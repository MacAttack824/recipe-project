from managers.recipe_manager import RecipeManager
from repositories.memory_recipe_repo import MemoryRecipeRepo
import click

repo = MemoryRecipeRepo()

recipe_manager = RecipeManager(repository=repo)

@click.command()
@click.option('--name', prompt='Enter Recipe Name:')
def click_add_recipe(name:str):
    recipe_manager.add_recipe(name=name)
    

if __name__ == '__main__':

    for i in range(2):
        click_add_recipe(standalone_mode=False)

    recipe_manager.repository.get_all()

@click.command()
@click.option('--basic_ingredients', prompt='Enter Basic Ingredients (comma separated):')
def click_add_basic_ingredients(basic_ingredients:list):
    recipe_manager.add_basic_ingredients(basic_ingredients=basic_ingredients.split(','))

    for i in range(2):
        click_add_basic_ingredients(standalone_mode=False)

    recipe_manager.repository.get_all()

    