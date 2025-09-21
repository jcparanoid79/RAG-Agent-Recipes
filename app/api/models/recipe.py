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

class Recipe(BaseModel):
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

class RecipeResponse(BaseModel):
    recipes: List[Recipe]
    
    class Config:
        schema_extra = {
            "example": {
                "recipes": [
                    {
                        "title": "Chicken and Rice",
                        "ingredients": ["chicken", "rice", "onions", "garlic"],
                        "instructions": "1. Cook rice according to package instructions.\n2. Season chicken with salt and pepper.\n3. In a large skillet, sauté onions and garlic until fragrant.\n4. Add chicken and cook until golden brown.\n5. Combine chicken with rice and serve."
                    }
                ]
            }
        }