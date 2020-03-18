from application import db

gym_classes=db.Table('gym_classes',
db.Column('gym_id',db.Integer, db.ForeignKey('gym.gym_id')),
db.Column('classes_id',db.Integer, db.ForeignKey('classes.classes_id'))
)

class Gym(db.Model):
    gym_id = db.Column(db.Integer, primary_key=True)
    gym_name = db.Column(db.String(100), nullable=False, unique=True)
    postcode = db.Column(db.String(7), nullable=False, unique=True)


class Classes(db.Model):
    classes_id = db.Column(db.Integer, primary_key=True)
    activity= db.Column(db.String(30), nullable=False)
    date=db.Column(db.Integer)
    time=db.Column(db.Integer, nullable=False) 
