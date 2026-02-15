def add_recipe_mac():
    print('Adding Recipe')
    recipe_name = input('What is the Recipe name? : ')
    print(f'Finished adding {recipe_name}')
    return (f'*** {recipe_name}***')

def add_basic_ingredient():
    basic_ingredients = []
    print('now adding basic ingredients...')
    while True:
        new_basic_ingredient = input('What basic kitchen ingredients are needed? OR type done to finish: ')
        if new_basic_ingredient == 'done':
            break
        else:
            basic_ingredients.append(new_basic_ingredient)
    filtered_basic_ingredients = [item for item in basic_ingredients if item not in ("")]
    basic_ingredients = filtered_basic_ingredients
    print('...finished adding basic ingredients')
    return basic_ingredients

def add_ingredient():
    ingredients = []
    print('adding ingredients...')
    while True:
        new_ingredient = input('What grocery ingredients do you need to purchase? OR type done to finish: ')
        if new_ingredient == 'done':
            break
        else:
            ingredients.append(new_ingredient)
    filtered_ingredients = [item for item in ingredients if item not in ("")]
    ingredients = filtered_ingredients
    print('...finished adding ingredients')
    return ingredients

def add_cook_time():
    cook_time = input('How long does this meal take to prepare? (in minutes): ')
    cook_time = int(cook_time)
    return (f'*** {cook_time}***')

def add_steps():
    steps = []
    print('Creating Steps...')
    while True:
        new_step = input('Describe each step and hit enter OR type done to finish: ')
        if new_step == 'done':
            break
        else:
            steps.append(new_step)
    filtered_steps = [item for item in steps if item not in ("")]
    steps = filtered_steps
    print('...finished adding steps')
    return steps

def add_sides():
    sides = []
    print('Creating a list of sides...')
    while True:
        new_side = input('Add sides to go with the main dish, OR type done to finish: ')
        if new_side == 'done':
            break
        else:
            sides.append(new_side)
    filtered_sides = [item for item in sides if item not in ("")]
    sides = filtered_sides
    print('...finished adding sides')
    return sides



recipe_name = add_recipe_mac()
ingredients = add_ingredient()
basic_ingredients = add_basic_ingredient()
cook_time = add_cook_time()
steps = add_steps()
sides = add_sides()
print(recipe_name, ingredients, basic_ingredients, cook_time, steps, sides)