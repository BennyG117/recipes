from flask_app import app

from flask_app.controllers import user_controller
from flask_app.controllers import recipe_controller


if __name__ == "__main__":
    app.run(debug=True, port=5001)




    
# =========================================================
# REMEMBER TO IMPORT CONTROLLERS INTO YOUR SERVER FILE!
# =========================================================

# from flask_app.controllers import

# RUN pipenv install PyMySQL flask flask-bcrypt
# REMEMBER TO SAVE YOUR .mwb FILE TO THE FOLDER!

