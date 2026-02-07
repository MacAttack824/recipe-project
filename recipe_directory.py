# Here lies the recipe lists as a dictionary

#dataclass = __init__Recipe(self, 

recipe_file = dict(
	{{'name': 'tacos'},
	{'ID' : 1},
	{'basic_ingredients': ['oil', 'salt', 'pepper', 'hot sauce', 'sour cream', 'taco seasoning']},
	{'ingredients': ['protein', 'tortillas', 'tomatoes', 'lettuce', 'corn']},
	{'cook time': '25 minutes'},
	{'steps' : 'JUST COOK IT'},
	{'skill' : 'easy skill required'},
    {'suggested sides': ['rice', 'beans', 'guacamole', 'chips', 'salsa', ]}
	}
    
	{{'name': 'pancakes'},
	{'ID' : 2},
	{'basic_ingredients': ['oil, butter, milk, eggs']},
    {'ingredents': ['pancake mix']},
    {'cook time': '20 minutes'},
    {'steps' : ['measure amount of pancake mix and mix well in a bowl', 'Add some oil to the pan and dollop a fist sized amount to start the pancake',
              'once you see bubbles popping, it should be ready to flip to cook the other']},
    {'skill' : 'medium skill required'},
    {'suggestedsides': ['bacon', 'eggs', 'sausage', 'fruit', 'yogurt', 'biscuits']}
	}
)


for recipe in recipe_file:
    print(recipe['name'])
