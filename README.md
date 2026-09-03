# Dinner Chooser 9000

Dinner Chooser 9000 (DC9) is a family meal-planning application designed to answer the recurring question: **What are we having for dinner?**

The long-term goal is to bring our family's recipes together in one searchable database, make it easy to plan anywhere from one night to a full week, and turn the chosen meals into a single useful shopping list.

## The Problem DC9 Solves

Choosing dinners for the week can be repetitive and time-consuming. Even after the meals are chosen, someone still has to open every recipe, compare ingredient lists, and work out what needs to be purchased.

DC9 is intended to make that process simple:

1. Choose how many days to plan, from **1 to 7**.
2. Browse the full recipe collection or narrow the choices by cuisine and tags.
3. Randomly generate the requested number of different meals from the available recipes.
4. Review the suggested meal plan.
5. Temporarily keep any individual meals—one, several, or all of them.
6. Redraw only the meal slots not being kept while the selected meals remain in place.
7. Repeat the keep-and-redraw process until the family is happy with the plan.
8. Confirm the final choices.
9. View or print one combined ingredient list for every selected recipe.

## Core Features

### Meal planning

- Plan meals for 1–7 days.
- Randomly select the requested number of recipes.
- Avoid selecting the same recipe twice in one meal plan.
- Temporarily keep any number of suggested meals.
- Redraw only the remaining meal slots without losing the meals already kept.
- Continue keeping and redrawing recipes until the user confirms the complete plan.
- Display the final meal plan in a clear, printable format.

### Recipe discovery

- Search or browse recipes by name.
- Filter recipes by cuisine, such as `Mexican` or `Italian`.
- Filter recipes by one or more descriptive tags, such as `easy`, `quick`, or `game day`.
- Use filtered search results to choose a recipe directly or narrow the pool used by the random meal generator.

### Combined shopping list

- Collect the ingredients from every recipe in the confirmed meal plan.
- Combine matching ingredients when practical.
- Include quantities and measurements when that information is available.
- Keep fresh or store-bought ingredients separate from pantry staples.
- Produce one list that can be viewed or printed for shopping.

### Recipe management

DC9 will allow recipes to be:

- Added
- Viewed
- Edited
- Deleted

Each recipe may include:

- Recipe name
- Fresh or store-bought ingredients
- Pantry ingredients
- Quantities and measurements
- Cooking time
- Step-by-step instructions
- Difficulty level
- Cuisine and descriptive tags, such as `Mexican`, `Italian`, `easy`, or `game day`
- Suggested side dishes
- An optional scanned recipe or printable source document

## Data Storage

All recipe and meal-planning data is stored in **Supabase**, which provides the project's hosted PostgreSQL database.

The planned data model separates recipes, ingredients, instructions, tags, and related information so that recipes can share ingredients without storing unnecessary duplicates. A recipe-to-ingredient relationship can also hold details such as quantity and unit of measurement.

Supabase connection values are loaded from environment variables and must not be committed to the repository. The `.env` file should remain listed in `.gitignore`.

## Current Project Status

DC9 is under active development as both a useful family tool and a database/programming learning project.

The current command-line application can collect recipe information and save recipe data to Supabase. The database structure and recipe-management flows are still evolving. Meal-plan confirmation, combined ingredient handling, printable output, and richer recipe organization are planned as the project grows.

## Planned Development

- Complete the View, Add, Edit, and Delete recipe workflows.
- Finalize the relational database design.
- Store ingredients through a normalized recipe-ingredient relationship.
- Add quantity and measurement data.
- Add cuisines and flexible recipe tags.
- Search, browse, and filter recipes by name, cuisine, and tags.
- Generate meal plans for a user-selected 1–7 day period.
- Allow the user to temporarily keep any suggested meals and redraw only the remaining choices.
- Repeat partial redraws until the user confirms the complete meal plan.
- Combine the selected recipes into one organized shopping list.
- Add clean printing or export options for meal plans, shopping lists, and recipes.
- Improve the interface beyond the initial command-line version.

## Project Vision

DC9 is not meant to be merely a random recipe picker. It is intended to become a practical household tool that preserves family recipes, introduces more variety into weekly dinners, reduces the effort of meal planning, and makes grocery preparation faster.

The project is also a place to practice Python application design, relational database modeling, repository patterns, Git, and Supabase while building something the family can genuinely use.
