""" This script generates images with text using PIL. """
import os
from app import create_app  # Import the create_app function
from PIL import Image, ImageDraw, ImageFont
from flask import current_app

# Define function to create images
def generate_image(image_path, text, size=(500, 500), background_color=(255, 255, 255), text_color=(0, 0, 0)):
    """Generates an image with text"""
    
    app = create_app()  # Create an instance of the Flask application

    with app.app_context():
        # Create a blank image with the specified background color
        img = Image.new('RGB', size, color=background_color)
        # Initialize ImageDraw
        d = ImageDraw.Draw(img)
        
        # Create an instance of the font
        font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 12)  # Full path on macOS
         
        # Calculate text size and position
        text_bbox = d.textbbox((0, 0), text, font=font)  # Get bounding box of text
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (size[0] - text_width) // 2
        text_y = (size[1] - text_height) // 2
        
        # Draw the text on the image
        d.text((text_x, text_y), text, fill=text_color, font=font)
       
        directory = os.path.dirname(image_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        # Save the image
        img.save(image_path)

# Example usage
elements = [
    {'image_file': 'images/a.png', 'text_description': 'A'},
    {'image_file': 'images/b.png', 'text_description': 'B'},
    {'image_file': 'images/c.png', 'text_description': 'C'},
    {'image_file': 'images/d.png', 'text_description': 'D'},
    {'image_file': 'images/e.png', 'text_description': 'E'},
    {'image_file': 'images/f.png', 'text_description': 'F'},
    {'image_file': 'images/g.png', 'text_description': 'G'},
    {'image_file': 'images/h.png', 'text_description': 'H'},
    {'image_file': 'images/i.png', 'text_description': 'I'},
    {'image_file': 'images/j.png', 'text_description': 'J'},
    {'image_file': 'images/k.png', 'text_description': 'K'},
    {'image_file': 'images/l.png', 'text_description': 'L'},
    {'image_file': 'images/m.png', 'text_description': 'M'},
    {'image_file': 'images/n.png', 'text_description': 'N'},
    {'image_file': 'images/o.png', 'text_description': 'O'},
    {'image_file': 'images/p.png', 'text_description': 'P'},
    {'image_file': 'images/q.png', 'text_description': 'Q'},
    {'image_file': 'images/r.png', 'text_description': 'R'},
    {'image_file': 'images/s.png', 'text_description': 'S'},
    {'image_file': 'images/t.png', 'text_description': 'T'},
    {'image_file': 'images/u.png', 'text_description': 'U'},
    {'image_file': 'images/v.png', 'text_description': 'V'},
    {'image_file': 'images/w.png', 'text_description': 'W'},
    {'image_file': 'images/x.png', 'text_description': 'X'},
    {'image_file': 'images/y.png', 'text_description': 'Y'},
    {'image_file': 'images/z.png', 'text_description': 'Z'},
    {'image_file': 'images/1.png', 'text_description': '1'},
    {'image_file': 'images/2.png', 'text_description': '2'},
    {'image_file': 'images/3.png', 'text_description': '3'},
    {'image_file': 'images/4.png', 'text_description': '4'},
    {'image_file': 'images/5.png', 'text_description': '5'},
    {'image_file': 'images/6.png', 'text_description': '6'},
    {'image_file': 'images/7.png', 'text_description': '7'},
    {'image_file': 'images/8.png', 'text_description': '8'},
    {'image_file': 'images/9.png', 'text_description': '9'},
    {'image_file': 'images/10.png', 'text_description': '10'},
    {'image_file': 'images/apple.png', 'text_description': 'apple'},
    {'image_file': 'images/banana.png', 'text_description': 'banana'},
    {'image_file': 'images/cherry.png', 'text_description': 'cherry'},
    {'image_file': 'images/orange .png', 'text_description': 'orange'},
    {'image_file': 'images/kiwi.png', 'text_description': 'kiwi'},
    {'image_file': 'images/strawberry.png', 'text_description': 'strawberry'},
    {'image_file': 'images/grapes.png', 'text_description': 'grapes'},
    {'image_file': 'images/mango.png', 'text_description': 'mango'},
    {'image_file': 'images/pear.png', 'text_description': 'pear'},
    {'image_file': 'images/pineapple.png', 'text_description': 'pineapple'},
    {'image_file': 'images/watermelon.png', 'text_description': 'watermelon'},
    {'image_file': 'images/tomato.png', 'text_description': 'tomato'},
    {'image_file': 'images/bell_pepper.png', 'text_description': 'bell_pepper'},
    {'image_file': 'images/carrot.png', 'text_description': 'carrot'},
    {'image_file': 'images/potato.png', 'text_description': 'potato'},
    {'image_file': 'images/onion.png', 'text_description': 'onion'},
    {'image_file': 'images/eggplant.png', 'text_description': 'eggplant'},
    {'image_file': 'images/cucumber.png', 'text_description': 'cucumber'},
    {'image_file': 'images/lettuce.png', 'text_description': 'lettuce'},
    {'image_file': 'images/broccoli.png', 'text_description': 'broccoli'},
    {'image_file': 'images/spinach.png', 'text_description': 'spinach'},
    {'image_file': 'image/red.png', 'text_description': 'Red'},
    {'image_file': 'image/blue.png', 'text_description': 'Blue'},
    {'image_file': 'image/green.png', 'text_description': 'Green'},
    {'image_file': 'image/yellow.png', 'text_description': 'Yellow'},
    {'image_file': 'image/orange.png', 'text_description': 'Orange'},
    {'image_file': 'image/purple.png', 'text_description': 'Purple'},
    {'image_file': 'image/pink.png', 'text_description': 'Pink', },
    {'image_file': 'image/brown.png', 'text_description': 'Brown', },
    {'image_file': 'image/black.png', 'text_description': 'Black'},
    {'image_file': 'image/white.png', 'text_description': 'White'},
    {'image_file': 'image/circle.png', 'text_description': 'Circle'},
    {'image_file': 'image/square.png', 'text_description': 'Square'},
    {'image_file': 'image/triangle.png', 'text_description': 'Triangle', },
    {'image_file': 'image/rectangle.png', 'text_description': 'Rectangle'},
    {'image_file': 'image/star.png', 'text_description': 'Star'},
    {'image_file': 'image/heart.png', 'text_description': 'Heart'},
    {'image_file': 'image/oval.png', 'text_description': 'Oval'},
    {'image_file': 'image/diamond.png', 'text_description': 'Diamond'},
    {'image_file': 'image/pentagon.png', 'text_description': 'Pentagon'},
    {'image_file': 'image/hexagon.png', 'text_description': 'Hexagon'},
    {'image_file': 'image/head.png', 'text_description': 'Head'},
    {'image_file': 'image/eyes.png', 'text_description': 'Eyes'},
    {'image_file': 'image/nose.png', 'text_description': 'Nose'},
    {'image_file': 'image/mouth.png', 'text_description': 'Mouth'},
    {'image_file': 'image/ears.png', 'text_description': 'Ears'},
    {'image_file': 'image/hands.png', 'text_description': 'Hands'},
    {'image_file': 'image/legs.png', 'text_description': 'Legs'},
    {'image_file': 'image/feet.png', 'text_description': 'Feet'},
    {'image_file': 'image/toes.png', 'text_description': 'Toes'},
    {'image_file': 'image/fingers.png', 'text_description': 'Fingers'},
    {'image_file': 'image/car.png', 'text_description': 'Car'},
    {'image_file': 'image/bus.png', 'text_description': 'Bus'},
    {'image_file': 'image/truck.png', 'text_description': 'Truck'},
    {'image_file': 'image/motorcycle.png', 'text_description': 'Motorcycle'},
    {'image_file': 'image/bicycle.png', 'text_description': 'Bicycle'},
    {'image_file': 'image/train.png', 'text_description': 'Train'},
    {'image_file': 'image/image/airplane.png', 'text_description': 'Airplane'},
    {'image_file': 'image/image/helicopter.png', 'text_description': 'Helicopter'},
    {'image_file': 'image/image/boat.png', 'text_description': 'Boat'},
    {'image_file': 'image/image/ship.png', 'text_description': 'Ship'},
    {'image_file': 'image/image/dog.png', 'text_description': 'Dog'},
    {'image_file': 'image/image/cat.png', 'text_description': 'Cat'},
    {'image_file': 'image/image/elephant.png', 'text_description': 'Elephant'},
    {'image_file': 'image/image/lion.png', 'text_description': 'Lion'},
    {'image_file': 'image/horse.png', 'text_description': 'Horse'},
    {'image_file': 'image/corcodile.png', 'text_description': 'Corcodile',},
    {'image_file': 'image/zebra.png', 'text_description': 'Zebra'},
    {'image_file': 'image/snail.png', 'text_description': 'Snail' },
    {'image_file': 'image/cow.png', 'text_description': 'Cow'},
    {'image_file': 'image/monkey.png', 'text_description': 'Monkey'},
    ]
# Generate images for each element
def upload_images_to_db():
    """     img = Image.new('RGB', size, color=background_color)
    q = ImageDraw.Draw(img)            
    for element in elements:
        generate_image(element['image_file'], element['text_description'])
    """
    # Add your code here to upload images to the database

    for element in elements:
        generate_image(element['image_file'], element['text_description'])
    
if __name__ == '__main__':
    upload_images_to_db()
