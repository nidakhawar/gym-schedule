from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Classes, Gym

class GymForm(FlaskForm):
    gym_name = StringField('Gym Name',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    postcode = StringField('Postcode',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit = SubmitField('Add')

class ClassesForm(FlaskForm):
    activity = StringField('Activity',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    date = StringField('Date',
        validators = [
            DataRequired()
        ]
    )
    time = StringField('Time',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField('Add')
