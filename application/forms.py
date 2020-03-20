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

class UpdateGymForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
