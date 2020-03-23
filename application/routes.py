# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Gym, Classes
from application.forms import GymForm, ClassesForm, UpdateGymForm, DeleteGymForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    
    gymData = Gym.query.all()
    classesData = Classes.query.all()
    return render_template('home.html', title='Home', gym=gymData, classes=classesData)

@app.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DeleteGymForm()
    print (form.gym_id.data)
    print (form.validate_on_submit())
    if form.validate_on_submit():
        gymid = form.gym_id.data
        gymData=Gym.query.filter_by(gym_id=gymid).first()
        
        db.session.delete(gymData)
        
        db.session.commit()
        
        return redirect(url_for('gym'))

    return render_template('delete.html', title='Delete', form=form)


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateGymForm()
    gymData = Gym.query.all()
    if form.validate_on_submit():
        gymid=form.gym_id.data
        gymData=Gym.query.filter_by(gym_id=gymid).first()
        gymData.gym_name=form.gym_name.data,
        gymData.postcode=form.postcode.data
        
        db.session.commit()
        
        return redirect_for("/")
        
    return render_template('update.html', title='Update', form=form)

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
        gymdetails = Gym.query.all()
        gymdetails = Gym.query.filter_by(gym_id = gymdetails.gym_id).first()
        classesData = Classes(
            activity = form.activity.data,
            date = form.date.data,
            time = form.time.data,
            gymplan = gym_id
            
        )

        db.session.add(classesData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('classes.html', title='Classes', form=form)