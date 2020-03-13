from application import db
from application.models import Gym, Classes, Users


db.drop_all()
db.create_all()