from recipe_directory import Recipe
from repositories.memory_recipe_repo import MemoryRecipeRepo
from elements_of_recipe import add_basic_ingredient, add_ingredient, add_cook_time, add_steps




class RecipeManager:   
    def __init__(self, repository: MemoryRecipeRepo):
        self.repository = repository

    def add_recipe(self, name: str):
        
        ingredients = add_ingredient()
        basic_ingredients = add_basic_ingredient()
        cook_time = add_cook_time()
        steps = add_steps()
        #sides = add_sides()
        #tags = add_tags()

        print(f'adding recipe named {name}') 
        recipe = Recipe(name=name, basic_ingredients=basic_ingredients, ingredients=ingredients, cook_time=cook_time, steps=steps)
        self.repository.add(recipe=recipe)

