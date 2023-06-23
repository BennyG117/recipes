from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

from flask_bcrypt import Bcrypt  # Only needed on routes related to login/reg
bcrypt = Bcrypt(app)

# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================



# Home Route
@app.route('/')
def input_home():
    return render_template("login.html")


#route to login (HOME)


#route to all Recipes (aka DASHBOARD)























# Route to save registration information
@app.route('/register_user', methods=['POST'])
def successful_register():
    #go back to home is not a registered user or info is wrong
    if not User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    #! may need to add at end of thread above: ".decode('utf-8')"
    
    #adjust based on table (auto fields are id, create, updated - don't need to be added)
    newUser_data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    #make the user
    user_id = User.save(newUser_data)
    
    #putting user into session
    session['user_id'] = user_id

    #successfully taken to dashboard to see all recipes
    return redirect(f'/dashboard')


#route for user to create a new recipe through the "+ CREATE" a-tag button
@app.route('/createNew', methods=['POST'])
def add_recipe():
    print(request.form)
    Recipe.save(request.form)
    return redirect(f'/dashboard/{user_id}')


# route to have any user view a specific recipe
@app.route('/viewOne/<int:id>')
def show_recipe(id):
    return render_template('viewRecipe.html', recipe = Recipe.get_one_recipe({"id":id}))


#route to have a specific user edit a specific recipe
@app.route('/editOne/<int:id>')
def edit_recipe(id):
    return render_template('editRecipe.html', recipe = Recipe.)


# ====================================
# Log In Validations Route
# ====================================

# Route for login validation check for user login 
@app.route('/login_user', methods=['POST'])
def loginCheck():

    #check if email exists in db
    login_data = {'email':request.form['email']}
    user_in_db = User.get_oneByEmail(login_data)

    if not user_in_db: 
        #flash messages have category*
        flash('Invalid Email/Password', 'login')
        return redirect('/')

    # check if unhashed pw correct
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')

    #if valid then progress...    
    session['user_id'] = user_in_db.id
    
    return redirect('/dashboard')


# Route to successful login / Transfers user to success page
@app.route('/login')
def show_login():

        if 'user_id' not in session:
            flash('Please login or Register', 'warning')
            return redirect('/')
        newUser = User.get_oneById({'id': session['user_id']})

        return render_template('dashboard.html', newUser=newUser)


# ====================================
# Log Out & Clear Route
# ====================================

# Route to log out
@app.route('/logout')
def logout():
    session.clear()
    # may require session.pop('first_name / or other key:id') #
    return redirect('/')

# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================
