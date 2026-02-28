from managers.recipe_manager import RecipeManager
from repositories.memory_recipe_repo import MemoryRecipeRepo
import click
from welcome_prompts import welcome_prompt
#from recipe_directory import print_out

repo = MemoryRecipeRepo()

recipe_manager = RecipeManager(repository=repo)

@click.command()
@click.option('--name', prompt='Enter Recipe Name:')
def click_add_recipe(name:str):
    recipe_manager.add_recipe(name=name)
    


if __name__ == '__main__':

    welcome_prompt()

    for i in range(2):
        click_add_recipe(standalone_mode=False)
    #    print_out()
    recipe_manager.repository.get_all()
