# AI Recipe Agent REST API

## Overview
This project converts the existing Streamlit-based AI Recipe Agent into a RESTful API service using FastAPI. The API allows programmatic access to recipe recommendations based on user-provided ingredients.

## Features
- Retrieve recipes based on ingredients
- Health check endpoint
- JSON response format
- Error handling and validation
- Built with FastAPI for high performance

## API Endpoints

### Get Recipe by Ingredients
- **Endpoint**: `POST /api/v1/recipes`
- **Description**: Retrieve a recipe based on provided ingredients
- **Request Body**:
  ```json
  {
    "ingredients": ["chicken", "rice", "onions"]
  }
  ```
- **Response**:
  ```json
  {
    "title": "Chicken and Rice",
    "ingredients": ["chicken", "rice", "onions", "garlic"],
    "instructions": "1. Cook rice...\n2. Fry chicken...\n3. Combine and serve."
  }
  ```

### Health Check
- **Endpoint**: `GET /health`
- **Description**: Check if the service is running
- **Response**:
  ```json
  {
    "status": "healthy",
    "timestamp": "2023-01-01T00:00Z"
  }
  ```

## Getting Started

For a detailed step-by-step guide, see [STEP_BY_STEP_GUIDE.md](STEP_BY_STEP_GUIDE.md).

### Prerequisites
- Python 3.8+
- Google Gemini API key
- Required Python packages (see requirements.txt)

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` file:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```
4. Run the server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Testing the API
You can test the API using curl or any HTTP client:

```bash
# Health check
curl -X GET "http://localhost:8000/health"

# Get recipe
curl -X POST "http://localhost:8000/api/v1/recipes" \
  -H "Content-Type: application/json" \
  -d '{"ingredients": ["chicken", "rice"]}'
```

## Project Structure
```
RAG_Agent_Recipies/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── recipes.py   # Recipe-related endpoints
│   │   └── models/
│   │       ├── __init__.py
│   │       └── recipe.py    # Data models for requests/responses
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # Configuration settings
│   └── services/
│       ├── __init__.py
│       └── recipe_service.py # Business logic for recipe retrieval
├── plans/                   # Planning documents
│   ├── rest_api_design.md
│   ├── fastapi_structure_plan.md
│   ├── recipe_service_implementation.md
│   ├── error_handling_validation_plan.md
│   ├── api_documentation_plan.md
│   ├── api_testing_plan.md
│   ├── requirements_update_plan.md
│   ├── deployment_configuration_plan.md
│   └── complete_rest_api_plan.md
├── vector_db_sentence/      # Vector database
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md                # This file
```

## Error Handling
The API includes comprehensive error handling:
- 400 Bad Request: Invalid input data
- 422 Unprocessable Entity: Validation errors
- 500 Internal Server Error: Processing errors

## Development
To run in development mode with auto-reload:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
## Frontend Application
This project includes a web-based frontend application that allows users to:
- Capture images of ingredients using device camera
- Upload images of ingredients
- Automatically identify ingredients in images
- Retrieve recipes based on identified ingredients

### Frontend Files
The frontend is located in the `frontend/` directory and includes:
- `index.html` - Main application page
- `styles.css` - Styling and responsive design
- `app.js` - JavaScript functionality and API integration
- `README.md` - Frontend-specific documentation
- `DEPLOYMENT.md` - Deployment instructions

### Running the Frontend
1. Ensure the backend API is running (see Development section above)
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
3. Start a simple HTTP server:
   ```bash
   python -m http.server 8080
   ```
4. Open your web browser and navigate to `http://localhost:8080`

## API Documentation
FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License
This project is licensed under the MIT License.