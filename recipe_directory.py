from typing import Optional
from uuid import uuid1

class Ingredient:
    def __init__(self, name: str, measurement: Optional[str] = None):
        self.name = name
        self.measurement = measurement

class Recipe:
    def __init__(self, name: str, basic_ingredients: list[Ingredient], ingredients: list[Ingredient], cook_time: int, steps: list[str], suggested_sides: Optional[list[str]] = None, tags: Optional[list[str]] = None):
        self.name = name
        self.id = uuid1()
        self.basic_ingredients = basic_ingredients
        self.ingredients = ingredients
        self.cook_time = cook_time
        self.steps = steps
        self.suggested_sides = suggested_sides
        self.tags = tags

    def nametags(self):
        return '{} {}'.format(self.name, self.tags)
