from application import db


class Classes(db.Model):
    classes_id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.gym_id'), nullable=False)
    
    
    def __repr__(self):
        return ''.join([
            'Activity: ', self.name, '\r\n',
            'Date: ', self.date, '\r\n',
            'Time: ', self.time])

class Gym(db.Model):
    gym_id = db.Column(db.Integer, primary_key=True)
    gym_name = db.Column(db.String(100), nullable=False, unique=True)
    postcode = db.Column(db.String(7), nullable=False, unique=True)
    gym_plan = db.relationship('Classes',backref='gymplan', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'Gym Name: ',self.gym_name, '\r\n',
            'Postcode: ',self.postcode])