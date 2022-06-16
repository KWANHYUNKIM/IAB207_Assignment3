from flask import Blueprint, render_template, request, session
from .models import Destination 
from flask_login import login_required

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = Destination.query.all()
      
    return render_template('base.html',destinations=destinations)

@mainbp.route('/ticket')
def indext():
    destinations = Destination.query.all()
    
    return render_template('ticket.html',destinations=destinations)

@mainbp.route('/detail_event')
def detail_event():
    return render_template('event.html')
