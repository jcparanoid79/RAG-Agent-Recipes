from fastapi import APIRouter, HTTPException
from app.api.models.recipe import RecipeRequest, RecipeResponse
from app.services.recipe_service import RecipeService

router = APIRouter()
recipe_service = RecipeService()

@router.post("/recipes", response_model=RecipeResponse,
             summary="Get recipes by ingredients",
             description="Retrieve 3 recipes based on the provided ingredients. The AI will search through the recipe database to find the most relevant recipes that match the provided ingredients.",
             response_description="Returns a list of recipes with title, ingredients, and instructions")
async def get_recipes(recipe_request: RecipeRequest):
    try:
        result = recipe_service.get_recipes_by_ingredients(recipe_request.ingredients)
        return {"recipes": result["recipes"]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))