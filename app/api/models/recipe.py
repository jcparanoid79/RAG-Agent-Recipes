from pydantic import BaseModel
from typing import List, Optional

class RecipeRequest(BaseModel):
    ingredients: List[str]
    dietary_preferences: Optional[List[str]] = None
    
    class Config:
        schema_extra = {
            "example": {
                "ingredients": ["chicken", "rice", "onions"],
                "dietary_preferences": ["gluten-free"]
            }
        }

class RecipeResponse(BaseModel):
    title: str
    ingredients: List[str]
    instructions: str
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Chicken and Rice",
                "ingredients": ["chicken", "rice", "onions", "garlic"],
                "instructions": "1. Cook rice according to package instructions.\n2. Season chicken with salt and pepper.\n3. In a large skillet, sauté onions and garlic until fragrant.\n4. Add chicken and cook until golden brown.\n5. Combine chicken with rice and serve."
            }
        }

class ImageRequest(BaseModel):
    image_data: str  # Base64 encoded image
    prompt: Optional[str] = "Identify the food ingredients in this image. Return only the ingredient names in a comma-separated list. Do not include any other text."
    
    class Config:
        schema_extra = {
            "example": {
                "image_data": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/...",
                "prompt": "Identify the food ingredients in this image. Return only the ingredient names in a comma-separated list. Do not include any other text."
            }
        }

class ImageResponse(BaseModel):
    ingredients: List[str]
    
    class Config:
        schema_extra = {
            "example": {
                "ingredients": ["tomato", "onion", "garlic", "basil", "olive oil"]
            }
        }