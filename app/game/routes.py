import random  # Import the 'random' module
from flask import jsonify, Blueprint, render_template, session, redirect, url_for, flash, request
from flask_login import login_required
from ..models import db, ChildProfile, Category, Element

game = Blueprint('game', __name__)

@game.route('/')
def home():
    """ Show the home page """
    return render_template('home.html')

@game.route('/categories/<int:profile_id>')
@login_required
def categories(profile_id):
    """ Show the list of game categories """
    game_categories = Category.query.all()
    child = ChildProfile.query.get_or_404(profile_id)
    return render_template('categories.html', categories=game_categories, child_name=child.username, child_id=child.id)

@game.route('/select_category/<int:child_id>/<int:category_id>')
@login_required
def select_category(child_id, category_id):
    """ Select a specific category and redirect to the game dashboard """
    # Ensure the child_id is in the session
    if not session.get('child_id'):
        session['child_id'] = child_id

    return redirect(url_for('game.game_dashboard', child_id=child_id, category_id=category_id))

@game.route('/generate_audio/<text>', methods=['GET'])
@login_required
def generate_audio(text):
    """ Generate an audio file for the given text """
    # Construct the URL for the Responsive API
    audio_url = f"https://code.responsivevoice.org/getvoice.php?t={text}&tl=en&sv=male&key=SzVfLas9"
    return jsonify({'audio_url': audio_url})

@game.route('/about')
def about():
    """ Show the about page """
    return render_template('about.html')

@game.route('/game_dashboard/<int:child_id>/<int:category_id>')
@login_required
def game_dashboard(child_id, category_id):
    """ Show the game dashboard with the images and words """
    child = ChildProfile.query.get_or_404(child_id)
    category = Category.query.get_or_404(category_id)

    # Get a random element for the category
    correct_element = Element.query.filter_by(category_id=category.id).order_by(db.func.random()).first()

    # Generate audio URL for the correct element
    audio_url = url_for('generate_audio', text=correct_element.text_description)

    # Select two random incorrect elements (not the correct one)
    incorrect_elements = Element.query.filter(Element.category_id == category.id, Element.id != correct_element.id).order_by(db.func.random()).limit(2).all()

    # Combine correct and incorrect elements
    elements = incorrect_elements + [correct_element]

    # Shuffle elements so the correct one isn't always last
    random.shuffle(elements)

    # Pass the data to the template
    return render_template('dashboard.html', child=child, elements=elements, category=category, correct_element=correct_element, audio_url=audio_url)

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
