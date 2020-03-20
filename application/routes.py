# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Gym, Classes
from application.forms import GymForm, ClassesForm, UpdateGymForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    
    gymData = Gym.query.all()
    classesData = Classes.query.all()
    return render_template('home.html', title='Home', gym=gymData, classes=classesData)

@app.route('/delete/<int:gym_id>', methods=['POST'])
def delete(gym_id):

    gym_id = Gym.query.filter_by(gym_id=gym_id).first()
    db.session.delete(gym_id)
    db.session.commit()
    return redirect(url_for('gym'))


@app.route('/update/<int:gym_id>', methods=["POST"])
def update():
    form = UpdateGymForm()
    newgymname = request.form.get("newgymname")
    gym_name = request.form.get("gym_name")
    gym_name = Gym.query.filter_by(gym_name=gym_name).first()
    gymname.gym_id = newgymname
    db.session.commit()
    return redirect("/")


@app.route('/gym', methods=['GET', 'POST'])
def gym():
    form = GymForm()
    if form.validate_on_submit():
        gymData = Gym(
            gym_name = form.gym_name.data,
            postcode = form.postcode.data
            
        )

        db.session.add(gymData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('gym.html', title='Gym', form=form)


@app.route('/classes', methods=['GET', 'POST'])
def classes():
    form = ClassesForm()
    if form.validate_on_submit():
        classesData = Classes(
            activity = form.activity.data,
            date = form.date.data,
            time = form.time.data
            
        )

        db.session.add(classesData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('classes.html', title='Classes', form=form)