import os
from app import create_app
from app.models import Category, Element, db

# Add the app directory to the system path
app = create_app()
app.app_context().push()

def reset_and_insert_categories():
    """Reset and insert initial categories with icons from static."""
    print("Resetting and inserting categories...")

    # Clear existing categories
    Category.query.delete()

    # Define the path to the icons in the static folder
    image_path = os.path.join(os.getcwd(), 'app', 'static')

    # Create categories with icon paths
    categories = [
        {'name': 'Alphabet', 'icon': 'alphabet.png'},
        {'name': 'Numbers', 'icon': 'numbers.png'},
        {'name': 'Animals', 'icon': 'animals.png'},
        {'name': 'Fruits', 'icon': 'fruits.png'},
        {'name': 'Vegetables', 'icon': 'vegetables.png'},
        {'name': 'Colors', 'icon': 'colors.png'},
        {'name': 'Shapes', 'icon': 'shapes.png'},
        {'name': 'Body Parts', 'icon': 'body_parts.png'},
        {'name': 'Vehicles', 'icon': 'vehicles.png'},
    ]

    for category_data in categories:
        category = Category(
            name=category_data['name'],
            icon=os.path.join('image', category_data['icon'])  # Store relative icon path
        )
        db.session.add(category)

    db.session.commit()
    print("Categories inserted successfully!")

def upload_images_to_db():
    """Populate the database with elements using images from static."""
    print("Populating elements with images...")
    Element.query.delete()

    # Define the path to the images in the static folder
    image_path = os.path.join(os.getcwd(), 'app', 'static')
    elements = [
        {'image_file': 'A.png', 'text_description': 'A', 'category_name': 'Alphabet', 'audio_file': 'A.mp3'},
        {'image_file': 'B.png', 'text_description': 'B', 'category_name': 'Alphabet', 'audio_file': 'B.mp3'},
        {'image_file': 'C.png', 'text_description': 'C', 'category_name': 'Alphabet', 'audio_file': 'C.mp3'},
        {'image_file': 'D.png', 'text_description': 'D', 'category_name': 'Alphabet', 'audio_file': 'D.mp3'},
        {'image_file': 'E.png', 'text_description': 'E', 'category_name': 'Alphabet', 'audio_file': 'E.mp3'},
        { 'image_file': 'F.png', 'text_description': 'F', 'category_name': 'Alphabet', 'audio_file': 'F.mp3'},
        {'image_file': 'G.png', 'text_description': 'G', 'category_name': 'Alphabet', 'audio_file': 'G.mp3'},
        {'image_file': 'H.png', 'text_description': 'H', 'category_name': 'Alphabet', 'audio_file': 'H.mp3'},
        {'image_file': 'I.png', 'text_description': 'I', 'category_name': 'Alphabet', 'audio_file': 'I.mp3'},
        {'image_file': 'J.png', 'text_description': 'J', 'category_name': 'Alphabet', 'audio_file': 'J.mp3'},
        {'image_file': 'K.png', 'text_description': 'K', 'category_name': 'Alphabet', 'audio_file': 'K.mp3'},
        {'image_file': 'L.png', 'text_description': 'L', 'category_name': 'Alphabet', 'audio_file': 'L.mp3'},
        {'image_file': 'N.png', 'text_description': 'N', 'category_name': 'Alphabet', 'audio_file': 'N.mp3'},
        {'image_file': 'O.png', 'text_description': 'O', 'category_name': 'Alphabet', 'audio_file': 'O.mp3'},
        {'image_file': 'P.png', 'text_description': 'P', 'category_name': 'Alphabet', 'audio_file': 'P.mp3'},
        {'image_file': 'Q.png', 'text_description': 'Q', 'category_name': 'Alphabet', 'audio_file': 'Q.mp3'},
        {'image_file': 'R.png', 'text_description': 'R', 'category_name': 'Alphabet', 'audio_file': 'R.mp3'},
        {'image_file': 'S.png', 'text_description': 'S', 'category_name': 'Alphabet', 'audio_file': 'S.mp3'},
        {'image_file': 'T.png', 'text_description': 'T', 'category_name': 'Alphabet', 'audio_file': 'T.mp3'},
        {'image_file': 'U.png', 'text_description': 'U', 'category_name': 'Alphabet', 'audio_file': 'U.mp3'},
        {'image_file': 'V.png', 'text_description': 'V', 'category_name': 'Alphabet', 'audio_file': 'V.mp3'},
        {'image_file': 'W.png', 'text_description': 'W', 'category_name': 'Alphabet', 'audio_file': 'W.mp3'},
        {'image_file': '/X.png', 'text_description': 'X', 'category_name': 'Alphabet', 'audio_file': 'X.mp3'},
        {'image_file': 'Y.png', 'text_description': 'Y', 'category_name': 'Alphabet', 'audio_file': 'Y.mp3'},
        {'image_file': 'Z.png', 'text_description': 'Z', 'category_name': 'Alphabet', 'audio_file': 'Z.mp3'},
        {'image_file': 'one.png', 'text_description': 'One', 'category_name': 'Numbers', 'audio_file': '1.mp3'},
        {'image_file': 'two.png', 'text_description': 'Two', 'category_name': 'Numbers', 'audio_file': '2.mp3'},
        {'image_file': 'three.png', 'text_description': 'Three', 'category_name': 'Numbers', 'audio_file': '3.mp3'},
        {'image_file': 'four.png', 'text_description': 'Four', 'category_name': 'Numbers', 'audio_file': '4.mp3'},
        {'image_file': 'five.png', 'text_description': 'Five', 'category_name': 'Numbers', 'audio_file': '5.mp3'},
        {'image_file': 'six.png', 'text_description': 'Six', 'category_name': 'Numbers', 'audio_file': '6.mp3'},
        {'image_file': 'seven.png', 'text_description': 'Seven', 'category_name': 'Numbers', 'audio_file': '7.mp3'},
        {'image_file': 'eight.png', 'text_description': 'Eight', 'category_name': 'Numbers', 'audio_file': '8.mp3'},
        {'image_file': 'nine.png', 'text_description': 'Nine', 'category_name': 'Numbers', 'audio_file': '9.mp3'},
        {'image_file': 'ten.png', 'text_description': 'Ten', 'category_name': 'Numbers', 'audio_file': '10.mp3'},
        {'image_file': 'apple.png', 'text_description': 'Apple', 'category_name': 'Fruits', 'audio_file': 'apple.mp3'},
        {'image_file': 'banana.png', 'text_description': 'Banana', 'category_name': 'Fruits', 'audio_file': 'banana.mp3'},
        {'image_file': 'orange.png', 'text_description': 'Orange', 'category_name': 'Fruits', 'audio_file': 'orange.mp3'},
        {'image_file': 'grapes.png', 'text_description': 'Grapes', 'category_name': 'Fruits', 'audio_file': 'grapes.mp3'},
        {'image_file': 'strawberry.png', 'text_description': 'Strawberry', 'category_name': 'Fruits','audio_file': 'strawberry.mp3'},
        {'image_file': 'watermelon.png', 'text_description': 'Watermelon', 'category_name': 'Fruits', 'audio_file': 'watermelon.mp3'},
        {'image_file': 'pineapple.png', 'text_description': 'Pineapple', 'category_name': 'Fruits', 'audio_file': 'pineapple.mp3'},
        {'image_file': 'kiwi.png', 'text_description': 'Kiwi', 'category_name': 'Fruits', 'audio_file': 'kiwi.mp3'},
        {'image_file': 'cherry.png', 'text_description': 'Cherry', 'category_name': 'Fruits', 'audio_file': 'cherry.mp3'},
        {'image_file': 'mango.png', 'text_description': 'Mango', 'category_name': 'Fruits', 'audio_file': 'mango.mp3'},
        {'image_file': 'carrot.png', 'text_description': 'Carrot', 'category_name': 'Vegetables', 'audio_file': 'carrot.mp3'},
        {'image_file': 'broccoli.png', 'text_description': 'Broccoli', 'category_name': 'Vegetables', 'audio_file': 'broccoli.mp3'},
        {'image_file': 'cucumber.png', 'text_description': 'Cucumber', 'category_name': 'Vegetables', 'audio_file': 'cucumber.mp3'},
        {'image_file': 'tomato.png', 'text_description': 'Tomato', 'category_name': 'Vegetables', 'audio_file': 'tomato.mp3'},
        {'image_file': 'potato.png', 'text_description': 'Potato', 'category_name': 'Vegetables', 'audio_file': 'potato.mp3'},
        {'image_file': 'onion.png', 'text_description': 'Onion', 'category_name': 'Vegetables', 'audio_file': 'onion.mp3'},
        {'image_file': 'eggplant.png', 'text_description': 'Eggplant', 'category_name': 'Vegetables', 'audio_file': 'eggplant.mp3'},
        {'image_file': 'bell_pepper.png', 'text_description': 'Bell Pepper', 'category_name': 'Vegetables', 'audio_file': 'bell_pepper.mp3'},
        {'image_file': 'lemon.png', 'text_description': 'Lemon', 'category_name': 'Vegetables', 'audio_file': 'lemon.mp3'},
        {'image_file': 'spinach.png', 'text_description': 'Spinach', 'category_name': 'Vegetables', 'audio_file': 'spinach.mp3'},
        {'image_file': 'red.png', 'text_description': 'Red', 'category_name': 'Colors', 'audio_file': 'red.mp3'},
        {'image_file': 'blue.png', 'text_description': 'Blue', 'category_name': 'Colors', 'audio_file': 'blue.mp3'},
        {'image_file': 'green.png', 'text_description': 'Green', 'category_name': 'Colors', 'audio_file': 'green.mp3'},
        {'image_file': 'yellow.png', 'text_description': 'Yellow', 'category_name': 'Colors', 'audio_file': 'yellow.mp3'},
        {'image_file': 'orange.png', 'text_description': 'Orange', 'category_name': 'Colors', 'audio_file': 'orange.mp3'},
        {'image_file': 'purple.png', 'text_description': 'Purple', 'category_name': 'Colors', 'audio_file': 'purple.mp3'},
        {'image_file': 'pink.png', 'text_description': 'Pink', 'category_name': 'Colors', 'audio_file': 'pink.mp3'},
        {'image_file': 'brown.png', 'text_description': 'Brown', 'category_name': 'Colors', 'audio_file': 'brown.mp3'},
        {'image_file': 'black.png', 'text_description': 'Black', 'category_name': 'Colors', 'audio_file': 'black.mp3'},
        {'image_file': 'white.png', 'text_description': 'White', 'category_name': 'Colors', 'audio_file': 'white.mp3'},
        {'image_file': 'circle.png', 'text_description': 'Circle', 'category_name': 'Shapes', 'audio_file': 'circle.mp3'},
        {'image_file': 'square.png', 'text_description': 'Square', 'category_name': 'Shapes', 'audio_file': 'square.mp3'},
        {'image_file': 'triangle.png', 'text_description': 'Triangle', 'category_name': 'Shapes', 'audio_file': 'triangle.mp3'},
        {'image_file': 'rectangle.png', 'text_description': 'Rectangle', 'category_name': 'Shapes', 'audio_file': 'rectangle.mp3'},
        {'image_file': 'star.png', 'text_description': 'Star', 'category_name': 'Shapes', 'audio_file': 'star.mp3'},
        {'image_file': 'heart.png', 'text_description': 'Heart', 'category_name': 'Shapes', 'audio_file': 'heart.mp3'},
        {'image_file': 'oval.png', 'text_description': 'Oval', 'category_name': 'Shapes', 'audio_file': 'oval.mp3'},
        {'image_file': 'diamond.png', 'text_description': 'Diamond', 'category_name': 'Shapes', 'audio_file': 'diamond.mp3'},
        {'image_file': 'pentagon.png', 'text_description': 'Pentagon', 'category_name': 'Shapes', 'audio_file': 'pentagon.mp3'},
        {'image_file': 'hexagon.png', 'text_description': 'Hexagon', 'category_name': 'Shapes', 'audio_file': 'hexagon.mp3'},
        {'image_file': 'hair.png', 'text_description': 'hair', 'category_name': 'Body Parts', 'audio_file': 'hair.mp3'},
        {'image_file': 'eye.png', 'text_description': 'Eye', 'category_name': 'Body Parts', 'audio_file': 'eye.mp3'},
        {'image_file': 'nose.png', 'text_description': 'Nose', 'category_name': 'Body Parts', 'audio_file': 'nose.mp3'},
        {'image_file': 'mouth.png', 'text_description': ' Mouth', 'category_name': 'Body Parts', 'audio_file': 'mouth.mp3'},
        {'image_file': 'ear.png', 'text_description': 'Ear', 'category_name': 'Body Parts', 'audio_file': 'ear.mp3'},
        {'image_file': 'hand.png', 'text_description': 'Hands', 'category_name': 'Body Parts', 'audio_file': 'hand.mp3'},
        {'image_file': 'feet.png', 'text_description': 'Feet', 'category_name': 'Body Parts', 'audio_file': 'feet.mp3'},
        {'image_file': 'toes.png', 'text_description': 'Toes', 'category_name': 'Body Parts', 'audio_file': 'toes.mp3'},
        {'image_file': 'fingers.png', 'text_description': 'Fingers', 'category_name': 'Body Parts', 'audio_file': 'fingers.mp3'},
        {'image_file': 'arm.png', 'text_description': 'Arm', 'category_name': 'Body Parts', 'audio_file': 'arm.mp3'},
        {'image_file': 'car.png', 'text_description': 'Car', 'category_name': 'Vehicles', 'audio_file': 'car.mp3'},
        {'image_file': 'bus.png', 'text_description': 'Bus', 'category_name': 'Vehicles', 'audio_file': 'bus.mp3'},
        {'image_file': 'policecar.png', 'text_description': 'Policecar', 'category_name': 'Vehicles', 'audio_file': 'policecar.mp3'},
        {'image_file': 'fire_truck.png', 'text_description': 'fire_truck', 'category_name': 'Vehicles', 'audio_file': 'fire_truck.mp3'},
        {'image_file': 'bicycle.png', 'text_description': 'Bicycle', 'category_name': 'Vehicles', 'audio_file': 'bicycle.mp3'},
        {'image_file': 'train.png', 'text_description': 'Train', 'category_name': 'Vehicles', 'audio_file': 'train.mp3'},
        {'image_file': 'airplane.png', 'text_description': 'Airplane', 'category_name': 'Vehicles', 'audio_file': 'airplane.mp3'},
        {'image_file': 'helicopter.png', 'text_description': 'Helicopter', 'category_name': 'Vehicles', 'audio_file': 'helicopter.mp3'},
        {'image_file': 'boat.png', 'text_description': 'Boat', 'category_name': 'Vehicles', 'audio_file': 'boat.mp3'},
        {'image_file': 'ambulance.png', 'text_description': 'Ambulance', 'category_name': 'Vehicles', 'audio_file': 'ambulance.mp3'},
        {'image_file': 'dog.png', 'text_description': 'Dog', 'category_name': 'Animals', 'audio_file': 'dog.mp3'},
        {'image_file': 'cat.png', 'text_description': 'Cat', 'category_name': 'Animals', 'audio_file': 'cat.mp3'},
        {'image_file': 'elephant.png', 'text_description': 'Elephant', 'category_name': 'Animals', 'audio_file': 'elephant.mp3'},
        {'image_file': 'lion.png', 'text_description': 'Lion', 'category_name': 'Animals', 'audio_file': 'lion.mp3'},
        {'image_file': 'horse.png', 'text_description': 'Horse', 'category_name': 'Animals', 'audio_file': 'horse.mp3'},
        {'image_file': 'crocodile.png', 'text_description': 'Corcodile', 'category_name': 'Animals', 'audio_file': 'crocodile.mp3'},
        {'image_file': 'zebra.png', 'text_description': 'Zebra', 'category_name': 'Animals', 'audio_file': 'zebra.mp3'},
        {'image_file': 'snail.png', 'text_description': 'Snail', 'category_name': 'Animals', 'audio_file': 'snail.mp3'},
        {'image_file': 'cow.png', 'text_description': 'Cow', 'category_name': 'Animals', 'audio_file': 'cow.mp3'},
        {'image_file': 'monkey.png', 'text_description': 'Monkey', 'category_name': 'Animals', 'audio_file': 'monkey.mp3'},
        ]

    for element_data in elements:
        # Find the category by name
        category = Category.query.filter_by(name=element_data['category_name']).first()
        if category:
            element = Element(
                image_file=os.path.join(element_data['image_file']),
                audio_file = os.path.join(element_data['audio_file']),
                text_description=element_data['text_description'],
                category_id=category.id
            )
            db.session.add(element)

    db.session.commit()
    print("Elements inserted successfully!")

# Execute functions to reset and populate the database
reset_and_insert_categories()
upload_images_to_db()
print("Database populated successfully!")
