from typing import Optional
from uuid import uuid1

class Recipe:
    def __init__(self, name: str, basic_ingredients: list[str], ingredients: list[str], cook_time: int, steps: list[str], suggested_sides: Optional[list[str]] = None, tags: Optional[list[str]] = None):
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

    def print_out(self):
        print('************************')
        print(Recipe.name for recipe in self.recipes)
        print(f'This recipe takes about {cook_time} minutes to cook')
        print(f'This recipe has {len(steps)} steps')
        print('************************')

