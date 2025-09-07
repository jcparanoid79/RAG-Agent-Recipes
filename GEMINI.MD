# Project: AI Recipe Agent

---

### **General Instructions**

- You are an AI-powered engineering assistant. Your primary goal is to help me develop a Python-based recipe retrieval agent.
- You will assist by writing and modifying Python code, managing project dependencies, and explaining concepts.
- Always use Python for all code-related tasks.
- If a new dependency is required, please state the reason and provide the `pip install` command.
- When generating code, include clear comments and use modern Python syntax.

### **Mandatory Tools**

- **`shell`**: You must use the `shell` tool to execute all command-line commands.
- **`write-file`**: You must use the `write-file` tool to create new files or modify existing ones.
- **`read-file`**: You must use the `read-file` tool to read the contents of files in the project directory.

### **Initial Project Setup**

**Task:** Create the initial project structure and necessary files for the recipe agent.

**Steps:**

1.  Use `write-file` to create a `requirements.txt` file with the following content:
    - `langchain`
    - `langchain-google-genai`
    - `chromadb`
    - `pandas`
    - `streamlit`
2.  Use `shell` to install the dependencies from the `requirements.txt` file using the command: `pip install -r requirements.txt`.
3.  Use `write-file` to create a `recipes.csv` file with a few sample recipes to get us started. Include `title` and `ingredients` columns. Example rows:
    - `title: "Chicken and Rice", ingredients: "chicken, rice, onions, garlic"`
    - `title: "Roasted Vegetables", ingredients: "carrots, potatoes, olive oil, thyme"`
4.  Use `write-file` to create a new Python file named `agent.py` that will contain the core logic for the recipe agent. Use the Python code provided in our previous conversation, ensuring it uses the Gemini model for both embeddings and the LLM.
5.  After creating the `agent.py` file, provide a brief explanation of how to run the script.