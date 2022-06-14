#import flask module from Flask package
from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    
    #we use this utility module to display forms quickly
    bootstrap = Bootstrap(app)
    
    app.secret_key ='somerandomvalue'
    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///winery.sqlite'
    db.init_app(app)
    
    from . import views
    app.register_blueprint(views.mainbp)
    from . import auth
    app.register_blueprint(auth.bp)
    return app