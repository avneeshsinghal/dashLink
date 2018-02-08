import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()
class det(db.Document):
	age= db.StringField(max_length=60)
	name= db.StringField(max_length=60)
	gender=db.StringField(max_length=60)
	email= db.StringField(max_length=60)
	phone= db.StringField(max_length=60)
	address= db.StringField(max_length=60)
	ride_taken= db.StringField(max_length=60)
	user_plan= db.StringField(max_length=60)

class userDet(db.Document):
	age= db.StringField(max_length=60)
	name= db.StringField(max_length=60)
	gender=db.StringField(max_length=60)
	email= db.StringField(max_length=60)
	phone= db.StringField(max_length=60)
	address= db.StringField(max_length=60)
	ride_taken= db.StringField(max_length=60)
	user_plan= db.StringField(max_length=60)