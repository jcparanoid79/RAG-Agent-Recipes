import json
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()

class RecipeService:
    def __init__(self):
        # Get the Gemini API key from the environment variables
        gemini_api_key = os.getenv("GOOGLE_API_KEY")
        
        # Initialize the Gemini LLM
        self._llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)
        
        # Load the existing ChromaDB database
        embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self._vector_db = Chroma(persist_directory="./vector_db_sentence", embedding_function=embedding_function)
        
        # Create a retriever that returns 3 documents
        self._retriever = self._vector_db.as_retriever(search_kwargs={"k": 3})
        
        # Create a prompt template
        prompt_template = """
        You are an AI recipe assistant. A user will provide a list of ingredients, and you will try to find 3 relevant recipes from the provided context.
        You must return the recipes in a JSON format as a list with each recipe having the following keys: "title", "ingredients", and "instructions".
        
        Context: {context}
        Question: {question}
        
        Answer:
        """
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        
        # Create a RetrievalQA chain
        self._qa_chain = RetrievalQA.from_chain_type(
            self._llm,
            retriever=self._retriever,
            chain_type_kwargs={"prompt": PROMPT},
        )
    
    def get_recipes_by_ingredients(self, ingredients: list) -> dict:
        """
        Retrieve 3 recipes based on provided ingredients and save them to a JSON file.
        
        Args:
            ingredients (list): List of ingredient strings
            
        Returns:
            dict: Dictionary containing the list of recipes and the filename where they were saved
            
        Raises:
            ValueError: If ingredients list is empty or response parsing fails
            RuntimeError: If LLM or database operations fail
        """
        # Validate input
        if not ingredients or not isinstance(ingredients, list):
            raise ValueError("Ingredients must be a non-empty list")
        
        try:
            # Create a question for the chain
            ingredients_text = ", ".join(ingredients)
            question = f"Find 3 different recipes that use the following ingredients: {ingredients_text}"
            
            # Get the answer
            answer = self._qa_chain({"query": question})
            
            try:
                # Try to parse the JSON from the result
                result_text = answer["result"]
                
                # Handle markdown code blocks
                if result_text.startswith("```json"):
                    result_text = result_text[7:]  # Remove ```json
                if result_text.startswith("```"):
                    result_text = result_text[3:]  # Remove ```
                if result_text.endswith("```"):
                    result_text = result_text[:-3]  # Remove ```
                
                # Try to parse as a list of recipes first
                json_result = json.loads(result_text.strip())
                
                # If it's a single recipe, convert to a list
                if isinstance(json_result, dict) and "title" in json_result:
                    recipes = [json_result]
                # If it's already a list of recipes, use it
                elif isinstance(json_result, list):
                    recipes = json_result
                    # Ensure instructions is a string, not a list for each recipe
                    for recipe in recipes:
                        if isinstance(recipe.get("instructions"), list):
                            recipe["instructions"] = "\n".join(recipe["instructions"])
                else:
                    # Unexpected format, return as a single recipe in a list
                    recipes = [{
                        "title": "Recipe",
                        "ingredients": ingredients,
                        "instructions": str(json_result) if json_result else "No instructions available"
                    }]
                    
            except json.JSONDecodeError:
                # If the result is not a valid JSON, try to create a basic recipe structure
                # This mimics the behavior of the Streamlit app
                result_text = answer["result"]
                # Try to extract information from the text response
                # This is a simple fallback, in a real implementation you might want to use
                # a more sophisticated parsing approach
                recipes = [{
                    "title": "Recipe",
                    "ingredients": ingredients,
                    "instructions": result_text.strip() if result_text else "No instructions available"
                }]
            
            # Save recipes to a JSON file
            filename = f"recipes_{'_'.join(ingredients[:3])}.json"  # Use first 3 ingredients for filename
            # Replace any characters that might cause issues in filenames
            filename = filename.replace(" ", "_").replace("/", "_").replace("\\", "_")
            
            # Create the data to save
            data_to_save = {
                "ingredients": ingredients,
                "recipes": recipes
            }
            
            # Save to JSON file
            with open(filename, 'w') as f:
                json.dump(data_to_save, f, indent=2)
            
            # Return the recipes and filename
            return {
                "recipes": recipes,
                "filename": filename
            }
                
        except Exception as e:
            raise RuntimeError("Failed to retrieve recipes") from e