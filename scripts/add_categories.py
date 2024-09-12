import os
from app import create_app, db
from app.models import Category

app = create_app()
with app.app_context():
    # Path where category icons are stored
    icon_base_path = "static/icons"

    # Define the categories and their corresponding icon images
    categories = [
        {"name": "Numbers", "icon_image": "numbers.png"},
        {"name": "Letters", "icon_image": "letters.png"},
        {"name": "Animals", "icon_image": "animals.png"},
        {"name": "Vehicles", "icon_image": "vehicles.png"},
        {"name": "Colors", "icon_image": "colors.png"},
        {"name": "Shapes", "icon_image": "shapes.png"},
        {"name": "Fruits", "icon_image": "fruits.png"},
        {"name": "Objects", "icon_image": "objects.png"}
    ]

    # Add each category to the database
    for category_data in categories:
        icon_image_path = os.path.join(icon_base_path, category_data['icon_image']) 
        # Ensure the icon image file exists
        if not os.path.isfile(icon_image_path):
            print(f"Icon image file {icon_image_path} not found. Skipping...")
            continue
        category = Category(name=category_data['name'], icon_image=category_data['icon_image'])
        db.session.add(category)

    # Commit the changes
    db.session.commit()

    print("Categories with icons added successfully!")
