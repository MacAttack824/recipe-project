from typing import Optional

from elements_of_recipe import add_cook_time, add_steps


def print_out(recipes):
    print("************************")
    print(Recipe.name for recipe in recipes)
    print(f"This recipe takes about {add_cook_time} minutes to cook")
    print(f"This recipe has {len(add_steps)} steps")
    print("************************")


class Recipe:
    def __init__(
        self,
        recipe_name: str,
        cook_time: int,
        servings: int,
        cuisine_style: str,
        recipe_type: str,
        source_recipe_number: Optional[str] = None,
        ingredients: Optional[list["Ingredient"]] = None,
        steps: Optional[list[str]] = None,
        sides: Optional[list[str]] = None,
    ):
        self.recipe_name = recipe_name
        self.cook_time = cook_time
        self.servings = servings
        self.cuisine_style = cuisine_style
        self.recipe_type = recipe_type
        self.source_recipe_number = source_recipe_number
        self.ingredients = ingredients if ingredients is not None else []
        self.steps = steps if steps is not None else []
        self.sides = sides if sides is not None else []


class Ingredient:
    def __init__(
        self,
        ingredient_name: str,
        ingredient_type=None,
        ingredient_quantity=None,
        ingredient_unit=None,
        ing_preparation_notes: Optional[str] = None,
    ):
        self.ingredient_name = ingredient_name
        self.ingredient_type = ingredient_type
        self.ingredient_quantity = ingredient_quantity
        self.ingredient_unit = ingredient_unit
        self.ing_preparation_notes = ing_preparation_notes
