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

    for i in range(10):
        click_add_recipe(standalone_mode=False)

    recipe_manager.repository.get_all()
