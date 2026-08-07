import random


class MealPlanner:
    def __init__(self, recipe_repo):
        self.recipe_repo = recipe_repo

    def generate_meal_plan(self, number_of_days):
        if number_of_days < 1 or number_of_days > 7:
            raise ValueError("The number of days must be between 1 and 7.")

        recipes = self.recipe_repo.get_all()

        if number_of_days > len(recipes):
            raise ValueError("There are not enough recipes available.")

        meal_plan = random.sample(recipes, number_of_days)

        return meal_plan
