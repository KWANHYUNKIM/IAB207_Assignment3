from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')

# all winery information for client
class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    # ... Ticket Quantity / Ticket Price
    ticket_quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='destination')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key = True)
    buy_ticket = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default = datetime.now())
    #add the foreign keys
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    ticket_quantity = db.Column(db.Integer, db.ForeignKey('destinations.ticket_quantity'))

class Detail_Destination(db.Model):
     __tablename__ = 'details'
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(80))
     main_image = db.Column(db.String(200))
     sub_image = db.Column(db.String(200))
     description = db.Column(db.String(200))
     location = db.Column(db.String(200))
     when = db.Column(db.String(200))
     cost = db.Column(db.String(200))
     include = db.Column(db.String(200))
     what_you_receive = db.Column(db.String(200))
     event_registration = db.Column(db.String(200))
     covid_19 = db.Column(db.String(200))
     getting_around = db.Column(db.String(200))
     tags = db.Column(db.String(200))
     socialmedia = db.Column(db.String(200))
    