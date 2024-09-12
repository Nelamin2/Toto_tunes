from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegisterForm  # Forms for login and registration
from ..models import User  # Importing User model from the main application
from .. import db, bcrypt  # Importing bcrypt and database instances from the main app

auth = Blueprint('auth', __name__)

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have been logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

# Registration route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()  # Create a registration form instance
    if form.validate_on_submit():  # When form is submitted
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()  # Save user to the database
        flash('Your account has been created!', 'success')
        login_user(user)  # Automatically log the user in after registration
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)  # Render registration page with the form

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out', 'info')
    return redirect(url_for('main.home'))  # Redirect to home after logout

# create baby profile route
@auth.route('/createbabyprofile', methods=['GET', 'POST'])
@login_required  # Ensures only logged-in users can access
def set_baby_profile():
    form = BabyProfileForm()  # Create a form for the baby’s profile
    if form.validate_on_submit():
        baby_profile = ChildProfile(username=form.baby_name.data, gender=form.gender.data, age=form.age.data, parent=current_user)
        db.session.add(baby_profile)
        db.session.commit()
        flash('Baby profile updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('profile.html', form=form)

# baby profile route
@auth.route('/children')
@login_required
def view_children():
    # Get all child profiles for the current user
    children = ChildProfile.query.filter_by(user_id=current_user.id).all()
    return render_template('view_children.html', children=children)

@auth.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = BabyProfileForm()
    if form.validate_on_submit():
        current_user.baby_name = form.baby_name.data
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    return render_template('edit_profile.html', form=form)
