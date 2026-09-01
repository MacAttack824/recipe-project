from typing import Optional

# from uuid import uuid4
from elements_of_recipe import add_cook_time, add_steps
import random


def print_out(recipes):
    print("************************")
    print(Recipe.name for recipe in recipes)
    print(f"This recipe takes about {add_cook_time} minutes to cook")
    print(f"This recipe has {len(add_steps)} steps")
    print("************************")


class Recipe:
    def __init__(
        self,
        name: str,
        pantry_ingredients: list[str],
        ingredients: list[str],
        cook_time: int,
        steps: list[str],
        # suggested_sides: Optional[list[str]] = None,
        # tags: Optional[list[str]] = None,
    ):
        self.name = name
        # self.id = uuid4()
        self.pantry_ingredients = pantry_ingredients
        self.ingredients = ingredients
        self.cook_time = cook_time
        self.steps = steps
        # self.suggested_sides = suggested_sides
        # self.tags = tags

    def nametags(self):
        return "{} {}".format(self.name, self.tags)
