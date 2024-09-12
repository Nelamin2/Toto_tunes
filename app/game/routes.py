from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, ChildProfile

game = Blueprint('game', __name__)

@game.route('/')
def home():
    return render_template('home.html')

@game.route('/categories')
@login_required
def categories():
    # Show the game categories (e.g., music, shapes, etc.)
    categories = Category.query.all()
    return render_template('categories.html')

@game.route('/about')
def about():
    return render_template('about.html')

@game.route('/dashboard/<int:child_id>/<int:category_id>')
@login_required
def game_dashboard(child_id):
    child = ChildProfile.query.get_or_404(child_id)
    # Game dashboard for the selected child
    category = Category.query.get_or_404(category_id)
    correct_image = Image.query.filter_by(category_id=category.id, correct=True).order_by(db.func.random()).first()

    # Select two random incorrect images (not the correct one)
    incorrect_images = Image.query.filter(Image.category_id == category.id, Image.id != correct_image.id).order_by(db.func.random()).limit(2).all()

    # Combine correct and incorrect images
    images = incorrect_images + [correct_image]

    # Shuffle images so the correct one isn't always last
    random.shuffle(images)

    return render_template('dashboard.html', child=child, images=images, category=category, correct_image=correct_image)
    
    @game.route('/submit_answer/<int:child_id>/<int:category_id>', methods=['POST'])
    
@login_required
def result():
    # Final result page for the game
    # This could show the score, time taken, etc.
    return render_template('result.html')

def get_next_round(child_id, category_id):
    # Logic to decide whether to continue to the next round or end the game
    current_round = session.get('current_round', 1)
    total_rounds = 10  # Example: 5 rounds per game
    if current_round < total_rounds:
        session['current_round'] = current_round + 1
        return True
def submit_answer(child_id, category_id):
    selected_image_id = request.form.get('selected_image_id')  # Get the image ID the child selected
    correct_image_id = request.form.get('correct_image_id')  # Get the correct image ID

    child = ChildProfile.query.get_or_404(child_id)
    
    if selected_image_id == correct_image_id:
        # Increase the score and play congratulations sound
        session['score'] = session.get('score', 0) + 1
        flash('Correct! Good job!', 'success')
        # Optionally, play congratulations sound
    else:
        flash('Oops! The correct answer was the other one.', 'error')

    # Move to the next round or show the final result if this is the last round
    next_round = get_next_round(child_id, category_id)  # Function to get next round logic
    if next_round:
        return redirect(url_for('game.game_dashboard', child_id=child_id, category_id=category_id))
    else:
        return redirect(url_for('game.result', child_id=child_id))
def submit_answer(child_id, category_id):
    selected_image_id = request.form.get('selected_image_id')  # Get the image ID the child selected
    correct_image_id = request.form.get('correct_image_id')  # Get the correct image ID

    child = ChildProfile.query.get_or_404(child_id)
    
    if selected_image_id == correct_image_id:
        # Increase the score and play congratulations sound
        session['score'] = session.get('score', 0) + 1
        flash('Correct! Good job!', 'success')
        # Optionally, play congratulations sound
    else:
        flash('Oops! The correct answer was the other one.', 'error')

    # Move to the next round or show the final result if this is the last round
    next_round = get_next_round(child_id, category_id)  # Function to get next round logic
    if next_round:
        return redirect(url_for('game.game_dashboard', child_id=child_id, category_id=category_id))
    else:
        return redirect(url_for('game.result', child_id=child_id))



@game.route('/result')
@login_required
def result():
    # Final result page for the game
    # This could show the score, time taken, etc.
    return render_template('result.html')

def get_next_round(child_id, category_id):
    # Logic to decide whether to continue to the next round or end the game
    current_round = session.get('current_round', 1)
    total_rounds = 10  # Example: 5 rounds per game
    if current_round < total_rounds:
        session['current_round'] = current_round + 1
        return True
    else:
        return False
        
@game.route('/result/<int:child_id>')
@login_required
def result(child_id):
    # Show the final score or results
    score = session.get('score', 0)
    
    # Clear session variables for a new game
    session.pop('current_round', None)
    session.pop('used_image_ids', None)
    session.pop('score', None)

    return render_template('result.html', child_id=child_id, score=score)
