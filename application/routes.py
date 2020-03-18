# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Gym, Classes
from application.forms import GymForm, ClassesForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    GymData = Gym.query.all()
    return render_template('home.html', title='Home', gym=GymData)

    ClassesData = Classes.query.all()
    return render_template('home.html', title='Home', classes=ClassesData)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    gyms=Gym.query.filter_by(gymid=gym_id).first()
    db.session.delete(gyms)
    db.session.commit()
    return redirect(url_for('gym'))


@app.route('/gym', methods=['GET', 'POST'])
def gym():
    form = GymForm()
    if form.validate_on_submit():
        GymData = Gym(
            gym_name = form.gym_name.data,
            postcode = form.postcode.data
            
        )

        db.session.add(GymData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('gym.html', title='Gym', form=form)


@app.route('/classes', methods=['GET', 'POST'])
def classes():
    form = ClassesForm()
    if form.validate_on_submit():
        ClassesData = Classes(
            activity = form.activity.data,
            date = form.date.data,
            time = form.time.data
            
        )

        db.session.add(ClassesData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('gym.html', title='Gym', form=form)