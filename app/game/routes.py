import random  # Import the 'random' module
from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from flask_login import login_required
from ..models import db, ChildProfile, Category, Element

game = Blueprint('game', __name__)

@game.route('/')
def home():
    return render_template('home.html')

@game.route('/categories')
@login_required
def categories():
    """ Show the list of game categories """
    game_categories = Category.query.all()
    return render_template('categories.html', categories=game_categories)

@game.route('/select_category/<int:category_id>')
@login_required
def select_category(category_id):
    """ Select a specific category and redirect to the game dashboard """
    #category = Category.query.get_or_404(category_id)
    child_id = session.get('child_id')  # Assuming child ID is stored in session after login
    if not child_id:
        flash("Please select a profile before playing.", "warning")
        return redirect(url_for('game.categories'))

    return redirect(url_for('game.game_dashboard', child_id=child_id, category_id=category_id))

@game.route('/about')
def about():
    return render_template('about.html')

@game.route('/dashboard/<int:child_id>/<int:category_id>')
@login_required
def game_dashboard(child_id, category_id):
    child = ChildProfile.query.get_or_404(child_id)
    category = Category.query.get_or_404(category_id)

    # Fetch the correct image (use Element instead of Image)
    correct_image = Element.query.filter_by(category_id=category.id).order_by(db.func.random()).first()

    # Select two random incorrect images (not the correct one)
    incorrect_images = Element.query.filter(Element.category_id == category.id, Element.id != correct_image.id).order_by(db.func.random()).limit(2).all()

    # Combine correct and incorrect images
    images = incorrect_images + [correct_image]

    # Shuffle images so the correct one isn't always last
    random.shuffle(images)

    # Pass the audio file of the correct image
    correct_audio = correct_image.audio_file

    return render_template('dashboard.html', child=child, images=images, category=category, correct_image=correct_image, correct_audio=correct_audio)

@game.route('/submit_answer/<int:child_id>/<int:category_id>', methods=['POST'])
@login_required
def submit_answer(child_id, category_id):
    """ Handles the answer submission and scoring """
    selected_image_id = request.form.get('selected_image_id')  # Get the selected image ID
    correct_image_id = request.form.get('correct_image_id')  # Get the correct image ID

    if selected_image_id == correct_image_id:
        # Increase the score
        session['score'] = session.get('score', 0) + 1
        flash('Correct! Good job!', 'success')
    else:
        flash('Oops! The correct answer was the other one.', 'error')

    # Move to the next round or show the final result if this is the last round
    if get_next_round():
        return redirect(url_for('game.game_dashboard', child_id=child_id, category_id=category_id))
    else:
        return redirect(url_for('game.result', child_id=child_id))

@game.route('/result/<int:child_id>')
@login_required
def result(child_id):
    """ Shows the final score and resets the game session """
    score = session.get('score', 0)

    # Clear session variables for a new game
    session.pop('current_round', None)
    session.pop('used_image_ids', None)
    session.pop('score', None)

    return render_template('result.html', child_id=child_id, score=score)

def get_next_round():
    """ Logic to decide whether to continue to the next round or end the game """
    current_round = session.get('current_round', 1)
    total_rounds = 10  # Example: 10 rounds per game
    if current_round < total_rounds:
        session['current_round'] = current_round + 1
        return True
    else:
        return False
