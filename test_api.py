import requests
import json

# Test the health endpoint
try:
    response = requests.get("http://localhost:8000/health")
    print("Health endpoint response:")
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(f"Error testing health endpoint: {e}")

# Test the recipes endpoint
try:
    recipe_data = {
        "ingredients": ["chicken", "rice", "onions"]
    }
    
    response = requests.post(
        "http://localhost:8000/api/v1/recipes",
        headers={"Content-Type": "application/json"},
        data=json.dumps(recipe_data)
    )
    
    print("\nRecipes endpoint response:")
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.text)
except Exception as e:
    print(f"Error testing recipes endpoint: {e}")