import addons_list
import db
import odoo_manager

from flask import Flask, redirect, render_template, request, url_for

# creates a Flask application, named app
app = Flask(__name__)

@app.route("/")
def index():
    chapters = addons_list.get_modules()
    recipes = db.get_recipes()
    running_recipe = odoo_manager.get_running_recipe()
    return render_template('index.html', chapters=chapters, recipes=recipes, running_recipe=running_recipe)


@app.route("/completed")
def recipe_completed():
    recipe = request.args.get('recipe')
    if recipe:
        db.add_recipe(recipe)
    return redirect(url_for('index'))


@app.route("/incompleted")
def recipe_incompleted():
    recipe = request.args.get('recipe')
    if recipe:
        db.delete_recipe(recipe)
    return redirect(url_for('index'))


@app.route("/run")
def kill_odoo():
    path = request.args.get('path')
    if path:
        odoo_manager.run_odoo(path)
    return redirect(url_for('index'))


@app.route("/kill")
def run_odoo():
    odoo_manager.kill_odoo()
    return redirect(url_for('index'))


# run the application
if __name__ == "__main__":
    # odoo_manager.kill_odoo()
    app.run(debug=True)
