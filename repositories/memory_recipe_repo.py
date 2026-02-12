from recipe_directory import Recipe
from uuid import UUID 


class MemoryRecipeRepo:
    recipes: list[Recipe] = []

    def get_all(self):
        return self.recipes

    def get(self, recipe_id: UUID):
        
        recipe_found = None
        index_found = None
        for idx, recipe in enumerate(self.recipes):
            if recipe.id == recipe_id:
                recipe_found = recipe
                index_found = idx
        if not recipe_found or not index_found:
            raise KeyError('Recipe not found, check your ID')
        return self.recipes[index_found]


    def add(self, recipe: Recipe):
        self.recipes.append(recipe)

    def remove(self, recipe_id: UUID):
        recipe_found = None
        index_found = None
        for idx, recipe in enumerate(self.recipes):
            if recipe.id == recipe_id:
                recipe_found = recipe
                index_found = idx
        if not recipe_found or not index_found:
            raise KeyError('Recipe not found, check your ID')
        return self.recipes.pop(index_found)

    def edit(self, recipe_id: UUID, recipe: Recipe):
        recipe_found = None
        index_found = None
        for idx, recipe in enumerate(self.recipes):
            if recipe.id == recipe_id:
                recipe_found = recipe
                index_found = idx
        if not recipe_found or not index_found:
            raise KeyError('Recipe not found, check your ID')
        self.recipes[index_found] = recipe

