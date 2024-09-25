import os
from app import db
from app.models import Element, Category  # Assuming Category is defined
from flask import current_app

def upload_images_to_db():
    # Define the path to the static/images folder
    image_folder = os.path.join(current_app.root_path, 'static', 'images')

    # Get the category from the database (assuming it's already created)
    category = Category.query.filter_by(name='Fruits').first()  # Example for category
    
    # Iterate through the images in the static/images folder
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Extract the name of the image without extension
            name = os.path.splitext(filename)[0]
            
            # Check if the element already exists in the database to avoid duplicates
            element = Element.query.filter_by(name=name).first()
            
            if not element:
                # If the element does not exist, add it to the database
                new_element = Element(
                    name=name,
                    image_path=f'images/{filename}',  # Save relative path to image
                    category_id=category.id  # Assign the correct category ID
                )
                
                db.session.add(new_element)
                db.session.commit()
                print(f"Uploaded {name} to the database.")
            else:
                print(f"Element {name} already exists in the database.")

if __name__ == '__main__':
    upload_images_to_db()
