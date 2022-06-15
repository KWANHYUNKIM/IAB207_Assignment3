#import flask module from Flask package
from flask import Flask 
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()


#create a function that creates a web application
# a web server will run this web application
def create_app():
   
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    #we use this utility module to display forms quickly
    bootstrap = Bootstrap4(app)
    
    app.secret_key ='somerandomvalue'
    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///winery.sqlite'
    db.init_app(app)
    
     #initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from . import views
    app.register_blueprint(views.mainbp)
    from . import auth
    app.register_blueprint(auth.bp)
    return app

