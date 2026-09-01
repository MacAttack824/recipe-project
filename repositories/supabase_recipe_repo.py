from urllib import response

from supabase_client import supabase


class SupabaseRecipeRepo:
    def get_all(self):
        response = supabase.table("recipes").select("*").execute()

        return response.data

    def delete_recipe(self, recipe_id: int):
        response = supabase.table("recipes").delete().eq("id", recipe_id).execute()

        return response.data

    def add_recipe(self, recipe):
        response = (
            supabase.table("recipes")
            .insert(
                {
                    "recipe_name": recipe.name,
                    #                  "pantry_ingredients": recipe.pantry_ingredients,
                    #                   "ingredients": recipe.ingredients,
                    "cook_time": recipe.cook_time,
                    #                   "steps": recipe.steps,
                }
            )
            .execute()
        )

        return response.data
