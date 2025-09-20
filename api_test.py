import requests
import json

def test_api():
    """Test the AI Recipe Agent REST API"""
    
    # Test health endpoint
    print("Testing health endpoint...")
    response = requests.get("http://localhost:8001/health")
    print(f"Health check status: {response.status_code}")
    print(f"Health check response: {response.json()}")
    print()
    
    # Test recipe endpoint
    print("Testing recipe endpoint...")
    recipe_request = {
        "ingredients": ["chicken", "rice", "onions"]
    }
    
    response = requests.post(
        "http://localhost:8001/api/v1/recipes",
        json=recipe_request
    )
    
    print(f"Recipe request status: {response.status_code}")
    if response.status_code == 200:
        recipe = response.json()
        print("Recipe retrieved successfully:")
        print(f"Title: {recipe['title']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions: {recipe['instructions']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    
    print()
    
    # Test error case with empty ingredients
    print("Testing error case with empty ingredients...")
    error_request = {
        "ingredients": []
    }
    
    response = requests.post(
        "http://localhost:8001/api/v1/recipes",
        json=error_request
    )
    
    print(f"Error request status: {response.status_code}")
    if response.status_code == 422:
        print("Validation error correctly returned")
        print(f"Error details: {response.json()}")
    else:
        print(f"Unexpected response: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_api()