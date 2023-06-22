from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

#route to sucess (shows all recipes)
@app.route ('/allRecipes')
def successRecipes():
    all_recipes = Recipe.get_all_recipes()
    return render_template('success.html', all_recipes = all_recipes)


