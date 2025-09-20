import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.services.recipe_service import RecipeService

def test_recipe_service():
    """Test the recipe service implementation"""
    try:
        # Create an instance of the recipe service
        recipe_service = RecipeService()
        print("RecipeService initialized successfully")
        
        # Test with sample ingredients
        ingredients = ["chicken", "rice", "onions"]
        print(f"Testing with ingredients: {ingredients}")
        
        # Get a recipe
        recipe = recipe_service.get_recipe_by_ingredients(ingredients)
        print("Recipe retrieved successfully:")
        print(f"Title: {recipe.get('title', 'N/A')}")
        print(f"Ingredients: {recipe.get('ingredients', 'N/A')}")
        print(f"Instructions: {recipe.get('instructions', 'N/A')}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_recipe_service()