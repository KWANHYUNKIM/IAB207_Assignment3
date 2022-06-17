from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination, Comment, Ticket
from .forms import DestinationForm, CommentForm, TicketForm 
from . import db
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('ticket', __name__, url_prefix='/tickets')

@bp.route('/buying', methods = ['GET', 'POST'])
@login_required
def show(id):
    destination = Destination.query.filter_by(id=id).first()
    # create the comment form
    tform = TicketForm()    
    seller= Destination.query.filter_by(id=destination).first()  
    quantity =  Destination.query.filter_by(ticket_quantity=destination).first()  
    if tform.validate_on_submit():  
      #read the comment from the form
      ticket = Ticket(buy_ticket=tform.ticket_quantity.data,  
                        buyer_id=current_user,
                        seller_id=seller, 
                        ticket_quantity = quantity)
      
      db.session.add(Ticket) 
      db.session.commit() 
 
    print('Your comment has been added', 'success') 
    return render_template('tickets/booking_history.html', destination=destination, form=tform)


