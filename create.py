from application import db
from application.models import Gym, Classes


db.drop_all()
db.create_all()