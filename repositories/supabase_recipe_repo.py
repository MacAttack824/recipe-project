from urllib import response

from supabase_client import supabase


class SupabaseRecipeRepo:
    def get_all(self):
        response = supabase.table("recipes").select("*").execute()

        return response.data

    def delete_recipe(self, recipe_id: int):
        response = supabase.table("recipes").delete().eq("id", recipe_id).execute()

        return response.data
