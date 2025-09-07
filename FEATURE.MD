# **Feature Request: Gemini CLI Coder**

## **1\. Feature Description**

This feature enables the creation of a powerful, AI-driven command-line interface (CLI) development environment. It will leverage the Gemini CLI agent and a GEMINI.md context file to automate project setup, file creation, and code generation for a Python-based recipe agent. The goal is to streamline the development workflow and allow for a more natural, conversational approach to building software.

## **2\. User Stories**

* As a developer, I want to use natural language prompts to scaffold a new project, so that I can start coding faster without manual setup.  
* As a developer, I want to instruct the AI to create and modify project files based on a pre-defined GEMINI.md context, so that the code is consistent with my project's standards.  
* As a developer, I want the AI to handle routine tasks like dependency management and boilerplate code generation, so that I can focus on core application logic.

## **3\. Acceptance Criteria**

* \[ \] A GEMINI.md file must be created in the project root with clear instructions for the Gemini CLI agent.  
* \[ \] The GEMINI.md file must contain a section for "General Instructions" outlining the project's persona and goals.  
* \[ \] The GEMINI.md file must specify the "Mandatory Tools" to be used, such as shell, write-file, and read-file.  
* \[ \] The initial project setup commands must be included, instructing the agent to create requirements.txt and recipes.csv files with specified content.  
* \[ \] The agent must be instructed to create a Python file (agent.py) with the core logic for the recipe agent.  
* \[ \] A final instruction must be included to provide a brief explanation of how to run the completed agent script.

## **4\. Relevant Files**

* GEMINI.md (new file)  
* requirements.txt (new file)  
* recipes.csv (new file)  
* agent.py (new file)