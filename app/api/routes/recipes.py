from fastapi import APIRouter, HTTPException, UploadFile, File
from app.api.models.recipe import RecipeRequest, RecipeResponse, ImageRequest, ImageResponse
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

@router.post("/identify-ingredients", response_model=ImageResponse,
             summary="Identify ingredients in image",
             description="Identify food ingredients in an uploaded image using Google Gemini API.",
             response_description="Returns a list of identified ingredients")
async def identify_ingredients(image_request: ImageRequest):
    try:
        ingredients = recipe_service.identify_ingredients_in_image(
            image_request.image_data, 
            image_request.prompt if image_request.prompt is not None else "Identify the food ingredients in this image. Return only the ingredient names in a comma-separated list. Do not include any other text."
        )
        return ImageResponse(ingredients=ingredients)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))