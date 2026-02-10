# Here lies the recipes as a class

class Recipe:

	num_of_recipes = 0

	def __init__(self, name: str, page: int, basic_ing: list[str], ingredients: list[str], cook_time: int, steps: list[str], suggested_sides:list[str], tags: list[str]):
		self.name = name
		self.page = page
		self.basic_ing = basic_ing
		self.ingredients = ingredients
		self.cook_time = cook_time
		self.steps = steps
		self.suggested_sides = suggested_sides
		self.tags = tags
		Recipe.num_of_recipes += 1

def nametags(self):
    return '{} {}'.format(self.name, self.tags)

recipe_1 = Recipe('Tacos', 1, ['oil', 'salt', 'pepper', 'hot sauce', 'sour cream', 'taco seasoning'], ['protein', 'tortillas', 'tomatoes', 'lettuce', 'corn'], 25, 'JUST COOK IT', ['rice', 'beans', 'guacamole', 'chips', 'salsa'], ['easy skill', 'mexican'])

recipe_2 = Recipe('Pancakes', 2, ['oil, butter, milk, eggs'], ['pancake mix'], 20, ['measure amount of pancake mix and mix well in a bowl', 'Add some oil to the pan and dollop a fist sized amount to start the pancake',
'once you see bubbles popping, it should be ready to flip to cook the other'], ['bacon', 'eggs', 'sausage', 'fruit', 'yogurt', 'biscuits'], 'medium skill')

recipe_738 = Recipe('Cheeseburger Calzones', 738, ['flour', 'salt', 'pepper', 'oil', 'ketchup'], ['ground beef', 'cream cheese', 'shredded cheese', 'pickles', 'steak seasoning', 'pizza dough'], 60, 'steps', ['1000 island dressing', 'chips'], ['medium skill', 'tailgate party', 'italian'])

print(f'There are {Recipe.num_of_recipes} recipes in the notebook.')

print(recipe_1.__dict__)

print(recipe_1.cook_time)
print(recipe_2.ingredients) 
print(recipe_1.name, f', ID page {recipe_1.page}')
print(recipe_738.name)
print(recipe_738.tags)
print(nametags(recipe_738))

