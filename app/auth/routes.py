""" Routes for the authentication blueprint """ 
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import logout_user, login_required, current_user, login_user
from .forms import LoginForm, RegisterForm, ChildProfileForm
from ..models import User, ChildProfile
from .. import db
auth = Blueprint('auth', __name__)

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Login route for the application """
    form = LoginForm()  # Initialize the login form
    if form.validate_on_submit():  # Only runs if form is valid
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()  # Query the database for the user
        if user and user.check_password(password):
            login_user(user)  # Use Flask-Login to log in the user
            flash("Login successful!")
            return redirect(url_for('auth.view_children'))  # Redirect to the dashboard or home page
        else:
            flash("Invalid credentials!")
    return render_template('login.html', form=form)

# Registration route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    """ Registration route for the application """
    form = RegisterForm()  # Initialize the registration form
    if form.validate_on_submit():  # Only runs if form is valid
        email = form.email.data
        password = form.password.data
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash("User already exists!")
            return redirect(url_for('auth.register'))

        # Create new user with the hashed password
        new_user = User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

# Logout route
@auth.route('/logout')
@login_required
def logout():
    """ Route to log out the user """
    logout_user()  # Log the user out
    flash('You have been logged out', 'info')
    return redirect(url_for('game.home'))  # Redirect to home page after logout

# Create child profile route
@auth.route('/create_child_profile', methods=['GET', 'POST'])
@login_required
def create_child_profile():
    """ Route to create a new child profile """
    form = ChildProfileForm()  # Create a form for the child's profile
    if form.validate_on_submit():
        child_profile = ChildProfile(username=form.username.data, gender=form.gender.data, age=form.age.data, user_id=current_user.id)
        db.session.add(child_profile)
        db.session.commit()
        print(f"Child profile created: {child_profile}")  # Debug statement
        flash('Child profile created successfully!', 'success')
        return redirect(url_for('auth.view_children'))  # Redirect to view all children profiles
    return render_template('create_child_profile.html', form=form)


# View all children route
@auth.route('/view_children')
@login_required
def view_children():
    """ Route to view all child profiles """
    profiles = ChildProfile.query.filter_by(user_id=current_user.id).all()
    print(f"Returning profiles: {profiles}")  # Debug print
    return render_template('view_children.html', profiles=profiles)

@auth.route('/select_profile', methods=['POST'])
@login_required
def select_profile():
    """ Handle profile selection and redirect to dashboard """
    profile_id = request.form.get('profile_id')
    if profile_id:
        # Fetch the selected profile
        profile = ChildProfile.query.get(profile_id)
        if profile and profile.user_id == current_user.id:
            # You might want to store the selected profile in the session or pass it to the dashboard
            session['selected_profile_id'] = profile_id  # Storing selected profile ID in session
            # Redirect to the dashboard
            return redirect(url_for('game.dashboard'))
    # If there's an issue, redirect back to view children with an error message
    flash('Invalid profile selection.', 'danger')
    return redirect(url_for('auth.view_children'))

# View specific child profile route
@auth.route('/view_child/<int:child_id>')
@login_required
def view_child(child_id):
    """ Route to view a specific child profile """
    child = ChildProfile.query.get_or_404(child_id)
    if child.user_id != current_user.id:
        flash('Unauthorized access!', 'warning')
        return redirect(url_for('auth.view_children'))
    return render_template('view_child_profile.html', child=child, child_id=child_id)


# Update child profile route
@auth.route('/update_child_profile/<int:child_id>', methods=['GET', 'POST'])
@login_required
def update_child_profile(child_id):
    """ Route to update a specific child's profile """
    child = ChildProfile.query.get_or_404(child_id)
    if child.user_id != current_user.id:
        flash('Unauthorized access!', 'warning')
        return redirect(url_for('auth.view_children'))
    form = ChildProfileForm(obj=child)  # Initialize form with the child profile data
    if form.validate_on_submit():
        child.username = form.username.data
        child.gender = form.gender.data
        child.age = form.age.data
        db.session.commit()
        flash('Child profile updated successfully!', 'success')
        return redirect(url_for('auth.view_child', child_id=child.id))  # Redirect to the updated child profile

    return render_template('edit_profile.html', form=form, child=child)
