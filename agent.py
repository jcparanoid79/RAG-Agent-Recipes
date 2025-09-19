
import streamlit as st
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
import json
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from the environment variables
gemini_api_key = os.getenv("GOOGLE_API_KEY")

# Set up the Streamlit app
st.title("AI Recipe Agent")
st.write("Enter your ingredients below (one per line) and I will find a recipe for you.")

# Initialize the Gemini LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_api_key)

# Load the existing ChromaDB database
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_db = Chroma(persist_directory="./vector_db_sentence", embedding_function=embedding_function)

# Create a retriever
retriever = vector_db.as_retriever()

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
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT},
)

# Get user input
user_ingredients = st.text_area("Ingredients:")

if user_ingredients:
    # Create a question for the chain
    question = f"Find a recipe that uses the following ingredients: {user_ingredients}"
    
    # Get the answer
    answer = qa_chain({"query": question})
    
    try:
        # Try to parse the JSON from the result
        json_result = json.loads(answer["result"])
        st.json(json_result)
    except json.JSONDecodeError:
        # If the result is not a valid JSON, display the raw string
        st.write(answer["result"])
