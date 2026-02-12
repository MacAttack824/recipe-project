from recipe_directory import Recipe
from repositories.memory_recipe_repo import MemoryRecipeRepo



class RecipeManager:
    def __init__(self, repository: MemoryRecipeRepo):
        self.repository = repository

    def add_recipe(self, name: str):
        print(f'adding recipe named {name}') 
        recipe = Recipe(name=name, basic_ingredients=[], ingredients=[], cook_time=123, steps=[])
        self.repository.add(recipe=recipe)

        






