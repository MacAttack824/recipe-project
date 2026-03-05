from managers.recipe_manager import RecipeManager
from repositories.memory_recipe_repo import MemoryRecipeRepo


repo = MemoryRecipeRepo()
recipe_manager = RecipeManager(repository=repo)


def welcome_prompt():
    print("Welcome to the Recipe Manager!")
    print(
        "You can Meal Plan, add recipes, view recipes, edit recipes, and delete recipes."
    )
    print(
        "*******************************************************************************"
    )
    desire = input(
        "What would you like to do today? Type a number for meals to plan or Type ADD, EDIT, or DELETE: "
    )

    if desire.lower() == "add":
        print("Great! Let's add a new recipe!")
        name = input("Enter the name of the recipe: ")
        recipe_manager.add_recipe(name=name)

    elif desire.lower() == "edit":
        print("Ok! Let's edit a recipe!")
        # MemoryRecipeRepo.edit()

    elif desire.lower() == "delete":
        print("Was it bad!? Let's delete a recipe!")
        # MemoryRecipeRepo.remove()

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
    else:
        print("I didn't understand that. Please try again.")
