from recipe_directory import Recipe

# from repositories.memory_recipe_repo import MemoryRecipeRepo
import elements_of_recipe


class RecipeManager:
    def __init__(self, repository):
        self.repository = repository

    def add_recipe(self, name: str):

        ingredients = elements_of_recipe.add_ingredient()
        pantry_ingredients = elements_of_recipe.add_pantry_ingredient()
        cook_time = elements_of_recipe.add_cook_time()
        steps = elements_of_recipe.add_steps()
        # sides = add_sides()
        # tags = add_tags()

        print(f"adding recipe named {name}")
        recipe = Recipe(
            name=name,
            pantry_ingredients=pantry_ingredients,
            ingredients=ingredients,
            cook_time=cook_time,
            steps=steps,
        )
        self.repository.add_recipe(recipe=recipe)

    def view_recipes(self):
        recipes = self.repository.get_all()

        if not recipes:
            print("No recipes found.")
            return

        print("\n***************************")
        print("       SAVED RECIPES      ")
        print("***************************")

        for recipe in recipes:
            print(
                f"{recipe['id']}: "
                f"{recipe['recipe_name'].title()} "
                f"- {recipe['cook_time']} minutes"
            )

        print("***************************\n")

    def delete_recipe(self, recipe_id):
        deleted = self.repository.delete_recipe(recipe_id)

        if deleted:
            recipe = deleted[0]
            name = recipe["recipe_name"].title()

            print("\n************************")
            print("      RECIPE DELETED")
            print("************************")
            print(f"Recipe #{recipe_id}: {name} has been removed.")
            print("************************\n")
        else:
            print(f"\nRecipe #{recipe_id} was not found.\n")
