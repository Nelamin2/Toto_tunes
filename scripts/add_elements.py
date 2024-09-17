""" This script is used to populate the database with categories and elements. """
import os
import sys
from app import create_app
from app.models import Category, Element, db

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app()
app.app_context().push()

def populate_db():
    """ Populate the database with categories and elements. """
    # Create categories
    categories = [
        {'name': 'Alphabet', 'icon': 'alphabet.png'},
        {'name': 'Numbers', 'icon': 'numbers.png'},
        {'name': 'Animals', 'icon': 'animals.png'},
        {'name': 'Fruits', 'icon': 'fruits.png'},
        {'name': 'Vegetables', 'icon': 'vegetables.png'},
        {'name': 'Colors', 'icon': 'colors.png'},
        {'name': 'Shapes', 'icon': 'shapes.png'},
        {'name': 'Body Parts', 'icon': 'body_parts.png'},
        {'name': 'vehicles', 'icon': 'vehicles.png'},
    ]
      # Ensure no duplicate categories
    existing_categories = {category.name for category in Category.query.all()}
    for category_data in categories:
        if category_data['name'] not in existing_categories:
            category = Category(name=category_data['name'], icon=category_data['icon'])
            db.session.add(category)
    db.session.commit()
    # Create a mapping of category names to category objects
    category_map = {category.name: category for category in Category.query.all()}

    # Create elements
    elements = [
        {'image_file': 'a.png', 'text_description': 'A', 'category_name': 'Alphabet'},
        {'image_file': 'b.png', 'text_description': 'B', 'category_name': 'Alphabet'},
        {'image_file': 'c.png', 'text_description': 'C', 'category_name': 'Alphabet'},
        {'image_file': 'd.png', 'text_description': 'D', 'category_name': 'Alphabet'},
        {'image_file': 'e.png', 'text_description': 'E', 'category_name': 'Alphabet'},
        {'image_file': 'f.png', 'text_description': 'F', 'category_name': 'Alphabet'},
        {'image_file': 'g.png', 'text_description': 'G', 'category_name': 'Alphabet'},
        {'image_file': 'h.png', 'text_description': 'H', 'category_name': 'Alphabet'},
        {'image_file': 'i.png', 'text_description': 'I', 'category_name': 'Alphabet'},
        {'image_file': 'j.png', 'text_description': 'J', 'category_name': 'Alphabet'},
        {'image_file': 'k.png', 'text_description': 'K', 'category_name': 'Alphabet'},
        {'image_file': 'l.png', 'text_description': 'L', 'category_name': 'Alphabet'},
        {'image_file': 'm.png', 'text_description': 'M', 'category_name': 'Alphabet'},
        {'image_file': 'n.png', 'text_description': 'N', 'category_name': 'Alphabet'},
        {'image_file': 'o.png', 'text_description': 'O', 'category_name': 'Alphabet'},
        {'image_file': 'p.png', 'text_description': 'P', 'category_name': 'Alphabet'},
        {'image_file': 'q.png', 'text_description': 'Q', 'category_name': 'Alphabet'},
        {'image_file': 'r.png', 'text_description': 'R', 'category_name': 'Alphabet'},
        {'image_file': 's.png', 'text_description': 'S', 'category_name': 'Alphabet'},
        {'image_file': 't.png', 'text_description': 'T', 'category_name': 'Alphabet'},
        {'image_file': 'u.png', 'text_description': 'U', 'category_name': 'Alphabet'},
        {'image_file': 'v.png', 'text_description': 'V', 'category_name': 'Alphabet'},
        {'image_file': 'w.png', 'text_description': 'W', 'category_name': 'Alphabet'},
        {'image_file': 'x.png', 'text_description': 'X', 'category_name': 'Alphabet'},
        {'image_file': 'y.png', 'text_description': 'Y', 'category_name': 'Alphabet'},
        {'image_file': 'z.png', 'text_description': 'Z', 'category_name': 'Alphabet'},
        {'image_file': 'cat.png', 'text_description': 'Cat', 'category_name': 'animals'},
        {'image_file': 'dog.png', 'text_description': 'Dog', 'category_name': 'animals'},
        {'image_file': 'elephant.png', 'text_description': 'Elephant', 'category_name': 'animals'},
        {'image_file': 'corcodile.png', 'text_description': 'Corcoldile', 'category_name': 'animals'},
        {'image_file': 'cow.png', 'text_description': 'Cow', 'category_name': 'animals'},
        {'image_file': 'fish.png', 'text_description': 'Fish', 'category_name': 'animals'},
        {'image_file': 'turtule.png', 'text_description': 'Turtle', 'category_name': 'animals'},
        {'image_file': 'horse.png', 'text_description': 'Horse', 'category_name': 'animals'},
        {'image_file': 'monkey.png', 'text_description': 'Monkey', 'category_name': 'animals'},
        {'image_file': 'lion.png', 'text_description': 'Lion', 'category_name': 'animals'},
        {'image_file': 'one.png', 'text_description': 'One', 'category_name': 'Numbers'},
        {'image_file': 'two.png', 'text_description': 'Two', 'category_name': 'Numbers'},
        {'image_file': 'three.png', 'text_description': 'Three', 'category_name': 'Numbers'},
        {'image_file': 'four.png', 'text_description': 'Four', 'category_name': 'Numbers'},
        {'image_file': 'five.png', 'text_description': 'Five', 'category_name': 'Numbers'},
        {'image_file': 'six.png', 'text_description': 'Six', 'category_name': 'Numbers'},
        {'image_file': 'seven.png', 'text_description': 'Seven', 'category_name': 'Numbers'},
        {'image_file': 'eight.png', 'text_description': 'Eight', 'category_name': 'Numbers'},
        {'image_file': 'nine.png', 'text_description': 'Nine', 'category_name': 'Numbers'},
        {'image_file': 'ten.png', 'text_description': 'Ten', 'category_name': 'Numbers'},
        {'image_file': 'apple.png', 'text_description': 'Apple', 'category_name': 'Fruits'},
        {'image_file': 'banana.png', 'text_description': 'Banana', 'category_name': 'Fruits'},
        {'image_file': 'grapes.png', 'text_description': 'Grapes', 'category_name': 'Fruits'},
        {'image_file': 'mango.png', 'text_description': 'Mango', 'category_name': 'Fruits'},
        {'image_file': 'orange.png', 'text_description': 'Orange', 'category_name': 'Fruits'},
        {'image_file': 'papaya.png', 'text_description': 'Papaya', 'category_name': 'Fruits'},
        {'image_file': 'pineapple.png', 'text_description': 'Pineapple', 'category_name': 'Fruits'},
        {'image_file': 'strawberry.png', 'text_description': 'Strawberry', 'category_name': 'Fruits'},
        {'image_file': 'watermelon.png', 'text_description': 'Watermelon', 'category_name': 'Fruits'},
        {'image_file': 'cherries.png', 'text_description': 'cherries', 'category_name': 'Fruits'},
        {'image_file': 'kiwi.png', 'text_description': 'kiwi', 'category_name': 'Fruits'},
        { 'image_file': 'carrot.png', 'text_description': 'Carrot', 'category_name': 'Vegetables'},
        { 'image_file': 'cucumber.png', 'text_description': 'Cucumber', 'category_name': 'Vegetables'},
        { 'image_file': 'onion.png', 'text_description': 'Onion', 'category_name': 'Vegetables'},
        { 'image_file': 'potato.png', 'text_description': 'Potato', 'category_name': 'Vegetables'},
        { 'image_file': 'tomato.png', 'text_description': 'Tomato', 'category_name': 'Vegetables'},
        { 'image_file': 'cabbage.png', 'text_description': 'cabbage', 'category_name': 'Vegetables'},
        { 'image_file': 'corn.png', 'text_description': 'corn', 'category_name': 'Vegetables'},
        { 'image_file': 'radish.png', 'text_description': 'radish', 'category_name': 'Vegetables'},
        { 'image_file': 'ladyfinger.png', 'text_description': 'Ladyfinger', 'category_name': 'Vegetables'},
        { 'image_file': 'spinach.png', 'text_description': 'Spinach', 'category_name': 'Vegetables'},
        { 'image_file': 'red.png', 'text_description': 'Red', 'category_name': 'Colors'},
        { 'image_file': 'blue.png', 'text_description': 'Blue', 'category_name': 'Colors'},
        { 'image_file': 'green.png', 'text_description': 'Green', 'category_name': 'Colors'},
        { 'image_file': 'yellow.png', 'text_description': 'Yellow', 'category_name': 'Colors'},
        { 'image_file': 'orange.png', 'text_description': 'Orange', 'category_name': 'Colors'},
        { 'image_file': 'black.png', 'text_description': 'Black', 'category_name': 'Colors'},
        { 'image_file': 'white.png', 'text_description': 'White', 'category_name': 'Colors'},
        { 'image_file': 'purple.png', 'text_description': 'Purple', 'category_name': 'Colors'},
        { 'image_file': 'brown.png', 'text_description': 'Brown', 'category_name': 'Colors'},
        { 'image_file': 'pink.png', 'text_description': 'Pink', 'category_name': 'Colors'},
        { 'image_file': 'triangle.png', 'text_description': 'Triangle', 'category_name': 'Shapes'},
        { 'image_file': 'circle.png', 'text_description': 'Circle', 'category_name': 'Shapes'},
        { 'image_file': 'square.png', 'text_description': 'Square', 'category_name': 'Shapes'},
        { 'image_file': 'rectangle.png', 'text_description': 'Rectangle', 'category_name': 'Shapes'},
        { 'image_file': 'oval.png', 'text_description': 'Oval', 'category_name': 'Shapes'},
        { 'image_file': 'star.png', 'text_description': 'Star', 'category_name': 'Shapes'},
        { 'image_file': 'heart.png', 'text_description': 'Heart', 'category_name': 'Shapes'},
        { 'image_file': 'pentagon.png', 'text_description': 'Pentagon', 'category_name': 'Shapes'},
        { 'image_file': 'Diamond.png', 'text_description': 'Diamond', 'category_name': 'Shapes'},
        { 'image_file': 'octagon.png', 'text_description': 'Octagon', 'category_name': 'Shapes'},
        { 'image_file': 'head.png', 'text_description': 'Head', 'category_name': 'Body Parts'},
        { 'image_file': 'eyes.png', 'text_description': 'Eyes', 'category_name': 'Body Parts'},
        { 'image_file': 'nose.png', 'text_description': 'Nose', 'category_name': 'Body Parts'},
        { 'image_file': 'mouth.png', 'text_description': 'Mouth', 'category_name': 'Body Parts'},
        { 'image_file': 'ears.png', 'text_description': 'Ears', 'category_name': 'Body Parts'},
        { 'image_file': 'hands.png', 'text_description': 'Hands', 'category_name': 'Body Parts'},
        { 'image_file': 'legs.png', 'text_description': 'Legs', 'category_name': 'Body Parts'},
        { 'image_file': 'feet.png', 'text_description': 'Feet', 'category_name': 'Body Parts'},
        { 'image_file': 'fingers.png', 'text_description': 'Fingers', 'category_name': 'Body Parts'},
        { 'image_file': 'toes.png', 'text_description': 'Toes', 'category_name': 'Body Parts'},
        { 'image_file': 'car.png', 'text_description': 'Car', 'category_name': 'Vehicles'},
        { 'image_file': 'bus.png', 'text_description': 'Bus', 'category_name': 'Vehicles'},
        { 'image_file': 'train.png', 'text_description': 'Train', 'category_name': 'Vehicles'},
        { 'image_file': 'aeroplane.png', 'text_description': 'Aeroplane', 'category_name': 'Vehicles'},
        { 'image_file': 'ship.png', 'text_description': 'Ship', 'category_name': 'Vehicles'},
        { 'image_file': 'bicycle.png', 'text_description': 'Bicycle', 'category_name': 'Vehicles'},
        { 'image_file': 'motorcycle.png', 'text_description': 'Motorcycle', 'category_name': 'Vehicles'},
        { 'image_file': 'scooter.png', 'text_description': 'Scooter', 'category_name': 'Vehicles'},
        { 'image_file': 'truck.png', 'text_description': 'Truck', 'category_name': 'Vehicles'},
        { 'image_file': 'rocket.png', 'text_description': 'Rocket', 'category_name': 'Vehicles'},
    ]
    for element_data in elements:
        category = category_map.get(element_data['category_name'])
        if category:
            element = Element(
                image_file=element_data['image_file'],
                text_description=element_data['text_description'],
                category=category
            )
            db.session.add(element)
    db.session.commit()

if __name__ == '__main__':
    populate_db()
