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
        
        # Create a retriever
        self._retriever = self._vector_db.as_retriever()
        
        # Create a prompt template
        prompt_template = """
        You are an AI recipe assistant. A user will provide a list of ingredients, and you will try to find a relevant recipe from the provided context.
        You must return the recipe in a JSON format with the following keys: "title", "ingredients", and "instructions".
        
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
    
    def get_recipe_by_ingredients(self, ingredients: list) -> dict:
        """
        Retrieve a recipe based on provided ingredients.
        
        Args:
            ingredients (list): List of ingredient strings
            
        Returns:
            dict: Recipe information with title, ingredients, and instructions
            
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
            question = f"Find a recipe that uses the following ingredients: {ingredients_text}"
            
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
                
                json_result = json.loads(result_text.strip())
                
                # Ensure instructions is a string, not a list
                if isinstance(json_result.get("instructions"), list):
                    json_result["instructions"] = "\n".join(json_result["instructions"])
                
                return json_result
            except json.JSONDecodeError:
                # If the result is not a valid JSON, try to create a basic recipe structure
                # This mimics the behavior of the Streamlit app
                result_text = answer["result"]
                # Try to extract information from the text response
                # This is a simple fallback, in a real implementation you might want to use
                # a more sophisticated parsing approach
                return {
                    "title": "Recipe",
                    "ingredients": ingredients,
                    "instructions": result_text.strip() if result_text else "No instructions available"
                }
                
        except Exception as e:
            raise RuntimeError("Failed to retrieve recipe") from e