from flask import Blueprint, render_template, request, session
#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    
    return render_template('main.html')

@mainbp.route('/login', methods = ['GET'])
def login():

    email = request.values.get("email")
    pwd = request.values.get("pwd")
    print ("email: {}\npassword= {}".format(email,pwd))
    
   
    return render_template('login.html')

@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'