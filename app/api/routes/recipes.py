from fastapi import APIRouter, HTTPException
from app.api.models.recipe import RecipeRequest, RecipeResponse
from app.services.recipe_service import RecipeService

router = APIRouter()
recipe_service = RecipeService()

@router.post("/recipes", response_model=RecipeResponse, 
             summary="Get recipe by ingredients",
             description="Retrieve a recipe based on the provided ingredients. The AI will search through the recipe database to find the most relevant recipe that matches the provided ingredients.",
             response_description="Returns a recipe with title, ingredients, and instructions")
async def get_recipe(recipe_request: RecipeRequest):
    try:
        recipe = recipe_service.get_recipe_by_ingredients(recipe_request.ingredients)
        return recipe
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))