# import render_template function from the flask module
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Gym, Classes, Users
from application.forms import GymForm, RegistrationForm, LoginForm, UpdateAccountForm, ClassesFrom

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    GymData = Gym.query.all()
    return render_template('home.html', title='Home', gym=GymData)

    ClassesData = classes.query.all()
    return render_template('home.html', title='Home', classes=ClassesData)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)


@app.route('/gym', methods=['GET', 'POST'])
@login_required
def gym():
    form = GymForm()
    if form.validate_on_submit():
        GymData = Gym(
            gym_name = form.name.data,
            postcode = form.postcode.data
            
        )

        db.session.add(GymData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('gym.html', title='Gym', form=form)

@app.route('/classes', methods=['GET', 'POST'])
@login_required
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

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name        
        form.email.data = current_user.email        
    return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
        user = current_user.id
        posts = Posts.query.filter_by(user_id=user)
        for post in posts:
                db.session.delete(post)
        account = Users.query.filter_by(id=user).first()
        logout_user()
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for('register'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))