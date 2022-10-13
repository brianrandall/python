from flask_app.controllers import user_routes, recipe_routes
from flask_app import app


if __name__=="__main__":
    app.run(debug=True)  