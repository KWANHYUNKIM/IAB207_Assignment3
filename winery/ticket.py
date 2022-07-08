from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination, Comment, Ticket
from .forms import DestinationForm, CommentForm, TicketForm 
from . import db
import os
#additional import:
from flask_login import login_required, current_user
# endpoint 
bp = Blueprint('ticket', __name__, url_prefix='/tickets')

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  id = 1;      
  destination = Destination.query.filter_by(id=id).first()
  print(current_user.name)
  # create the comment form
  tform = TicketForm()    
    
  if tform.validate_on_submit():  
    #read the comment from the form 
    print(tform.ticket_quantity.data)
    ticket = Ticket(    
                        buy_ticket=tform.ticket_quantity.data,  
                        buyer_id=current_user.name,
                        seller_id=destination.name, 
                        ticket_quantity = destination.ticket_quantity);
      
    db.session.add(ticket) 
    db.session.commit()
    print('Your comment has been added', 'success') 
    return redirect(url_for('main.index'))
  return render_template('destinations/create.html', form=tform)


