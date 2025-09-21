# AI Recipe Agent REST API - Step-by-Step Guide

This guide will walk you through setting up and using the AI Recipe Agent REST API, which converts ingredients into delicious recipes using Google's Gemini AI.

## Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- A Google Gemini API key
- Git (optional, for cloning the repository)
- Basic knowledge of command-line operations

## Step 1: Obtain a Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to "API Keys" in the sidebar
4. Click "Create API Key"
5. Copy the generated API key and save it securely

## Step 2: Clone or Download the Repository

### Option A: Clone the Repository (Recommended)
```bash
git clone <repository-url>
cd RAG_Agent_Recipies
```

### Option B: Download the Repository
1. Download the ZIP file from the repository
2. Extract it to a folder of your choice
3. Navigate to the extracted folder

## Step 3: Set Up the Python Environment

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

## Step 4: Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Step 5: Configure Environment Variables

1. Create a `.env` file in the project root directory
2. Add your Google API key to the file:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Step 6: Start the API Server

Run the FastAPI server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The server will start and display:
```
INFO:     Uvicorn running on http://0.0.0.0:800 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

## Step 7: Verify the API is Running

### Check Health Endpoint
Open your browser or use curl to verify the API is running:
```bash
curl -X GET "http://localhost:8000/health"
```

You should receive a response like:
```json
{
  "status": "healthy",
  "timestamp": "2023-01-01T00:00Z",
  "services": {
    "api": "healthy"
  }
}
```

### Access API Documentation
Visit these URLs in your browser:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Step 8: Get a Recipe

### Using cURL
To get a recipe based on ingredients:
```bash
curl -X POST "http://localhost:8000/api/v1/recipes" \
  -H "Content-Type: application/json" \
  -d '{"ingredients": ["chicken", "rice", "onions"]}'
```

### Using Python
Create a simple Python script:
```python
import requests

url = "http://localhost:8000/api/v1/recipes"
data = {
    "ingredients": ["chicken", "rice", "onions"]
}

response = requests.post(url, json=data)
if response.status_code == 200:
    recipe = response.json()
    print(f"Recipe: {recipe['title']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Instructions: {recipe['instructions']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

## Step 9: Example API Responses

### Successful Recipe Response
```json
{
  "title": "Simple Chicken and Rice",
  "ingredients": [
    "1 lb boneless, skinless chicken breasts, cut into 1-inch cubes",
    "1 medium onion, chopped",
    "1 cup long-grain rice",
    "2 cups chicken broth",
    "1 teaspoon salt",
    "1/2 teaspoon black pepper",
    "1 tablespoon olive oil"
  ],
  "instructions": "Heat olive oil in a large skillet over medium-high heat.\nAdd chicken and cook until browned on all sides.\nAdd onion and cook until softened, about 5 minutes.\nStir in rice, chicken broth, salt, and pepper.\nBring to a boil, then reduce heat to low, cover, and simmer for 15-20 minutes, or until rice is cooked through and liquid is absorbed.\nFluff with a fork and serve."
}
```

### Error Response
```json
{
  "detail": "Ingredients must be a non-empty list"
}
```

## Step 10: Testing with Different Ingredients

Try different combinations of ingredients:
```bash
# Pasta recipe
curl -X POST "http://localhost:8000/api/v1/recipes" \
  -H "Content-Type: application/json" \
  -d '{"ingredients": ["pasta", "tomato", "basil"]}'

# Vegetarian option
curl -X POST "http://localhost:8000/api/v1/recipes" \
  -H "Content-Type: application/json" \
  -d '{"ingredients": ["beans", "corn", "bell peppers"]}'
```

## Step 11: Containerized Deployment (Optional)

For production deployment, you can use Docker:

1. Build the Docker image:
   ```bash
   docker build -t recipe-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 -e GOOGLE_API_KEY=your_api_key_here recipe-api
   ```

3. Or use docker-compose:
   ```bash
   docker-compose up
   ```

## Step 12: Stopping the Service

To stop the API server:
- Press `CTRL+C` in the terminal where the server is running
- If using Docker, run `docker-compose down`

## Troubleshooting

### Common Issues and Solutions

1. **"Module not found" errors**
   - Ensure you've activated the virtual environment
   - Reinstall dependencies with `pip install -r requirements.txt`

2. **"400 Bad Request" errors**
   - Check that your ingredients list is not empty
   - Ensure proper JSON formatting

3. **"500 Internal Server Error"**
   - Verify your Google API key is correct and active
   - Check the server logs for detailed error messages

4. **Port already in use**
   - Change the port number: `uvicorn app.main:app --host 0.0.0.0 --port 8001`

## Next Steps

1. Explore the API documentation at http://localhost:8000/docs
2. Review the source code in the `app/` directory
3. Check the planning documents in the `plans/` folder for implementation details
4. Review the architecture diagram in `diagram.mmd`

## Support

For issues or questions about the AI Recipe Agent REST API:
1. Check the README.md for documentation
2. Review the planning documents in the `plans/` folder
3. Examine the source code for implementation details
4. Open an issue in the repository if you encounter bugs