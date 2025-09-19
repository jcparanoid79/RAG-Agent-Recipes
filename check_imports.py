import sys
print("Python executable:", sys.executable)
print("Python path:", sys.path)

try:
    import streamlit as st
    print("✓ streamlit imported successfully")
except ImportError as e:
    print("✗ streamlit import failed:", e)

try:
    from langchain_community.vectorstores import Chroma
    print("✓ langchain_community.vectorstores imported successfully")
except ImportError as e:
    print("✗ langchain_community.vectorstores import failed:", e)

try:
    from langchain_google_genai import GoogleGenerativeAI
    print("✓ langchain_google_genai imported successfully")
except ImportError as e:
    print("✗ langchain_google_genai import failed:", e)

try:
    from langchain.prompts import PromptTemplate
    print("✓ langchain.prompts imported successfully")
except ImportError as e:
    print("✗ langchain.prompts import failed:", e)

try:
    from langchain.chains import RetrievalQA
    print("✓ langchain.chains imported successfully")
except ImportError as e:
    print("✗ langchain.chains import failed:", e)

try:
    from langchain_community.embeddings import SentenceTransformerEmbeddings
    print("✓ langchain_community.embeddings imported successfully")
except ImportError as e:
    print("✗ langchain_community.embeddings import failed:", e)

try:
    from dotenv import load_dotenv
    print("✓ dotenv imported successfully")
except ImportError as e:
    print("✗ dotenv import failed:", e)

try:
    import google.generativeai as genai
    print("✓ google.generativeai imported successfully")
except ImportError as e:
    print("✗ google.generativeai import failed:", e)

try:
    from sentence_transformers import SentenceTransformer
    print("✓ sentence_transformers imported successfully")
except ImportError as e:
    print("✗ sentence_transformers import failed:", e)