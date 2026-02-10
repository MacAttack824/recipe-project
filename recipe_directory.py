# Here lies the recipe lists as a dictionary

class Recipe: 
	def __init__(self, name, id, basic_ing, ingredients, cook_time, steps, suggested_sides, tags):
		self.name = name
		self.id = id
		self.basic_ing = basic_ing
		self.ingredients = ingredients
		self.cook_time = cook_time
		self.steps = steps
		self.suggested_sides = suggested_sides
		self.tags = tags

def nametags(name, tags):
    return name + ' + ' + ', '.join(tags)


recipe_1 = Recipe('tacos', 1, ['oil', 'salt', 'pepper', 'hot sauce', 'sour cream', 'taco seasoning'], ['protein', 'tortillas', 'tomatoes', 'lettuce', 'corn'], '25 minutes', 'JUST COOK IT', ['rice', 'beans', 'guacamole', 'chips', 'salsa'], ['easy skill', 'mexican'])

recipe_2 = Recipe('pancakes', 2, ['oil, butter, milk, eggs'], ['pancake mix'], '20 minutes', ['measure amount of pancake mix and mix well in a bowl', 'Add some oil to the pan and dollop a fist sized amount to start the pancake',
'once you see bubbles popping, it should be ready to flip to cook the other'], ['bacon', 'eggs', 'sausage', 'fruit', 'yogurt', 'biscuits'], 'medium skill')

recipe_738 = Recipe('Cheeseburger Calzones', 738, ['flour', 'salt', 'pepper', 'oil', 'ketchup'], ['ground beef', 'cream cheese', 'shredded cheese', 'pickles', 'steak seasoning', 'pizza dough'], '60 minutes', 'steps', ['1000 island dressing', 'chips'], ['medium skill', 'tailgate party', 'italian'])

print(recipe_1.__dict__)
print(recipe_2.__dict__) 
print(recipe_1.name, recipe_1.id)
print(recipe_738.name)
print(recipe_738.tags)

print(nametags(recipe_1.name, recipe_1.tags))
