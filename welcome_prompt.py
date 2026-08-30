import sys
from managers.recipe_manager import RecipeManager

# from repositories.memory_recipe_repo import MemoryRecipeRepo
from repositories.supabase_recipe_repo import SupabaseRecipeRepo

repo = SupabaseRecipeRepo()
recipe_manager = RecipeManager(repository=repo)


def welcome_prompt():
    print("Welcome to the Recipe Manager!")
    print(
        "You can Meal Plan, add recipes, view recipes and saved recipes, edit recipes, and delete recipes."
    )
    print(
        "*******************************************************************************"
    )
    desire = input(
        "What would you like to do today? Type a number for meals to plan or Type VIEW, ADD, EDIT, or DELETE: "
    )

    if desire.lower() == "add":
        print("Great! Let's add a new recipe!")
        name = input("Enter the name of the recipe: ")
        recipe_manager.add_recipe(name=name)

    elif desire.lower() == "edit":
        print("Ok! Let's edit a recipe!")
        repo.edit()

    elif desire.lower() == "delete":
        print("Was it bad!? Let's delete a recipe!")

        recipe_manager.view_recipes()

        recipe_id = int(input("Enter the ID of the recipe you want to delete: "))
        recipe_manager.delete_recipe(recipe_id=recipe_id)

    elif desire.lower() == "view":
        print("Let's see what recipes we have already!")
        repo.get_all()
        recipe_manager.view_recipes()

    elif (
        desire == "1"
        or desire == "2"
        or desire == "3"
        or desire == "4"
        or desire == "5"
        or desire == "6"
        or desire == "7"
    ):
        print(f"Great! Let's plan meals for {desire} days!")
        desire_int = int(desire)
        days = desire_int
        print(days)

    elif desire.lower() == "exit":
        print("Goodbye!")
        sys.exit()
    else:
        print("I didn't understand that. Please try again.")
