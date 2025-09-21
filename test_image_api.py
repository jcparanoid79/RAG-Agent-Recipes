import requests
import json
import base64

# Test the health endpoint
try:
    response = requests.get("http://localhost:8000/health")
    print("Health endpoint response:")
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(f"Error testing health endpoint: {e}")

# Test the identify-ingredients endpoint with sample data
try:
    # Create a simple test image data (this is just placeholder data)
    # In a real test, you would load an actual image file
    test_image_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
    
    image_data = {
        "image_data": f"data:image/png;base64,{test_image_data}",
        "prompt": "Identify the food ingredients in this image. Return only the ingredient names in a comma-separated list. Do not include any other text."
    }
    
    response = requests.post(
        "http://localhost:8000/api/v1/identify-ingredients",
        headers={"Content-Type": "application/json"},
        data=json.dumps(image_data)
    )
    
    print("\nIdentify ingredients endpoint response:")
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.text)
except Exception as e:
    print(f"Error testing identify-ingredients endpoint: {e}")