# Project: AI Recipe Agent - Further Improvements

---

### **General Instructions**

- You are an AI-powered engineering assistant. Your primary goal is to help implement enhancements to the existing Python-based recipe retrieval agent.
- You will assist by writing and modifying Python code, managing project dependencies, and explaining concepts.
- Always use Python for all code-related tasks.
- If a new dependency is required, please state the reason and provide the `pip install` command.
- When generating code, include clear comments and use modern Python syntax.

### **Mandatory Tools**

- **`shell`**: You must use the `shell` tool to execute all command-line commands.
- **`write-file`**: You must use the `write-file` tool to create new files or modify existing ones.
- **`read-file`**: You must use the `read-file` tool to read the contents of files in the project directory.

### **Enhancement Implementation Tasks**

#### **Task 1: Enhanced User Interface**
Improve the Streamlit interface with better visual components and additional filters.

**Steps:**
1. Modify `agent.py` to include dietary preference filters (vegetarian, vegan, gluten-free, etc.)
2. Add ingredient quantity selectors or sliders for more precise matching
3. Implement a tabbed interface to separate search and results

#### **Task 2: Nutritional Information**
Add nutritional calculations and display to recipe results.

**Steps:**
1. Add a dependency on a nutrition database API or local nutrition data file
2. Modify the prompt template to request nutritional information
3. Update the UI to display nutritional values alongside recipes

#### **Task 3: User Profiles and Favorites**
Implement user profile storage and favorite recipe tracking.

**Steps:**
1. Add a dependency on a lightweight database like SQLite
2. Create functions to save and retrieve user preferences
3. Add UI components for rating recipes and marking favorites
4. Modify the search algorithm to prioritize favorited recipes

#### **Task 4: Meal Planning Features**
Add weekly meal planning capabilities with shopping list generation.

**Steps:**
1. Create a new `meal_planner.py` module
2. Implement functions for selecting recipes for a week
3. Add a shopping list generator that aggregates ingredients
4. Create a Streamlit interface for meal planning

#### **Task 5: Advanced Search Capabilities**
Implement fuzzy matching and more sophisticated search features.

**Steps:**
1. Add a dependency on a fuzzy matching library like `fuzzywuzzy`
2. Modify the retrieval logic to handle partial matches
3. Implement ingredient exclusion filters
4. Add search by cuisine type or cooking time

#### **Task 6: External API Integration**
Connect to external services for enhanced functionality.

**Steps:**
1. Research and select a grocery API for ingredient purchasing
2. Implement authentication for external services
3. Add UI components for purchasing ingredients
4. Handle API rate limits and error cases

#### **Task 7: Multi-Modal Features**
Add image recognition and voice input capabilities.

**Steps:**
1. Add dependencies for image processing and speech recognition
2. Implement image recognition for identifying ingredients from photos
3. Add voice input functionality for hands-free recipe search
4. Update the UI to include camera and microphone inputs

### **Implementation Guidelines**

- Always maintain backward compatibility with existing functionality
- Test each enhancement individually before combining
- Document new features in code comments
- Follow the existing code style and structure
- Handle errors gracefully with informative messages to users