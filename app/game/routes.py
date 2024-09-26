""" Game routes for the application """
from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from ..models import db, ChildProfile, Category, Element, Score
import random

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

@game.route('/about')
def about():
    """ Show the about page """
    return render_template('about.html')

@game.route('/select_category/<int:child_id>/<int:category_id>')
@login_required
def select_category(child_id, category_id):
    """ Select a specific category and reset the game for that category """
    session['child_id'] = child_id
    session['score'] = 0
    session['current_round'] = 1
    return redirect(url_for('game.game_dashboard', child_id=child_id, category_id=category_id))

@game.route('/game_dashboard/<int:child_id>/<int:category_id>')
@login_required
def game_dashboard(child_id, category_id):
    """ Show the game dashboard with a random question for the selected category """
    category = Category.query.get_or_404(category_id)

    # Check if the game has already reached the maximum rounds
    if session.get('current_round', 1) > 10:
        return redirect(url_for('game.result', child_id=child_id))

    # Randomly select the correct element
    correct_element = Element.query.filter_by(category_id=category.id).order_by(db.func.random()).first()

    # Handle the case where no element is found
    if not correct_element or not correct_element.audio_file:
        flash('No audio available for this element', 'error')
        return redirect(url_for('game.categories', profile_id=child_id))

    # Use a static audio file based on the correct element's description
    audio_url = url_for('static', filename='audio/' + correct_element.audio_file)

    # Randomly select two incorrect elements
    incorrect_elements = Element.query.filter(
        Element.category_id == category.id,
        Element.id != correct_element.id
    ).order_by(db.func.random()).limit(2).all()

    elements = incorrect_elements + [correct_element]
    random.shuffle(elements)  # Shuffle the order

    return render_template(
        'game_dashboard.html', 
        elements=elements,
        correct_element=correct_element,
        audio_url=audio_url,
        child_id=child_id,
        category_id=category_id,
        profile_id=child_id,
        score=session.get('score', 0)  # Pass the score to the template
    )


@game.route('/update_score/<int:score>', methods=['POST'])
@login_required
def update_score(score):
    session['score'] = score
    return jsonify(success=True)

@game.route('/fetch_new_question/<int:child_id>/<int:category_id>', methods=['GET'])
@login_required
def fetch_new_question(child_id, category_id):
    """ Fetch a new question for the game """
    category = Category.query.get_or_404(category_id)

    # Retrieve current round from session
    current_round = session.get('current_round', 1)

    # Check if maximum rounds have been reached
    if current_round > 10:
        return jsonify(success=False)  # No more questions available

    # Randomly select the correct element
    correct_element = Element.query.filter_by(category_id=category.id).order_by(db.func.random()).first()

    # Handle case where no element is found
    if not correct_element or not correct_element.audio_file:
        return jsonify(success=False)

    # Prepare images for the response
    incorrect_elements = Element.query.filter(
        Element.category_id == category.id,
        Element.id != correct_element.id
    ).order_by(db.func.random()).limit(2).all()

    # Ensure we have 2 incorrect answers to return with the correct answer
    if len(incorrect_elements) < 2:
        return jsonify(success=False)

    elements = incorrect_elements + [correct_element]
    random.shuffle(elements)  # Shuffle the order of elements

    # Prepare the HTML for the images
    images_html = ''.join(
        f'<div class="col-md-4">'
        f'<button id="{element.id}" class="btn btn-lg btn-primary" onclick="submitAnswer(\'{element.id}\')">'
        f'<img src="{url_for("static", filename="image/" + element.image_file)}" class="img-fluid" alt="{element.text_description}">'
        f'</button>'
        f'</div>'
        for element in elements
    )

    # Prepare the audio URL
    audio_url = url_for('static', filename='audio/' + correct_element.audio_file)

    # Return the success response with the necessary data
    return jsonify(success=True, images_html=images_html, category_id=category_id, correct_answer_id=correct_element.id, audio_url=audio_url)


@game.route('/fetch_score/<int:child_id>', methods=['GET'])
@login_required
def fetch_score(child_id, category_id):
    """ Fetch the current score """
    score_record = Score.query.filter_by(child_id=child_id, category_id=category_id).first()
    if score_record:
        return jsonify(score=score_record.score)
    else:
        return jsonify(score=0)

@game.route('/result/<int:profile_id>/<int:category_id>', methods=['GET'])
@login_required
def result(profile_id, category_id):
    """ Show the result page with the final score """
    score = session.get('score', 0)
    total_rounds = 10

    # Clear session variables for a new game
    session.pop('current_round', None)
    session.pop('used_image_ids', None)
    session.pop('score', None)

    return render_template('result.html', child_id=profile_id, category_id=category_id, score=score, total_rounds=total_rounds)

@game.route('/exit_game/<int:profile_id>', methods=['GET'])
def exit_game():
    """ Exit the game and redirect to the main page """
    return redirect(url_for('auth.home'))

