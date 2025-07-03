import csv
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app import models  # This will import all models from your __init__.py

# A simple script to seed materials from a CSV file.

# --- CONFIGURATION ---
CSV_FILE_PATH = "Material Test Database - Sheet1.csv"  # The name of your CSV file


def seed_materials():
    """
    Reads materials from a CSV and populates the database,
    handling the many-to-many relationship with vegetables.
    """
    db: Session = SessionLocal()
    print("Seeding materials from CSV...")

    try:
        with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            for row in reader:
                name, image, type_str, vegetable_ids_str = row

                # Clean up the data
                name = name.strip()
                image = image.strip() if image else None
                type_str = type_str.strip().lower()

                print(f"Processing material: {name}")

                # --- Core Many-to-Many Logic ---

                # 1. Find or create the Material object
                # This check prevents creating duplicate materials if you run the script again.
                material = db.query(models.Material).filter(
                    models.Material.name == name).first()
                if not material:
                    material = models.Material(
                        name=name, image=image, type=type_str)
                    db.add(material)
                    print(f"  - Creating new material: {name}")
                else:
                    print(f"  - Found existing material: {name}")

                # 2. Find all associated Vegetable objects
                if vegetable_ids_str:
                    vegetable_ids = [int(vid.strip())
                                     for vid in vegetable_ids_str.split(',')]

                    for veg_id in vegetable_ids:
                        vegetable = db.query(models.Vegetable).filter(
                            models.Vegetable.id == veg_id).first()

                        if vegetable:
                            # 3. Create the link
                            # Check if the link already exists before adding
                            if vegetable not in material.vegetables:
                                material.vegetables.append(vegetable)
                                print(
                                    f"    - Linking to vegetable ID: {veg_id} ({vegetable.name})")
                            else:
                                print(
                                    f"    - Link to vegetable ID: {veg_id} already exists. Skipping.")
                        else:
                            print(
                                f"    - WARNING: Vegetable with ID {veg_id} not found. Skipping.")

            # 4. Commit all changes for the session
            db.commit()

    except FileNotFoundError:
        print(f"Error: The file {CSV_FILE_PATH} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()
        print("Seeding complete. Database session closed.")


if __name__ == "__main__":
    # This makes sure the script can be run directly
    # It will create the tables if they don't exist based on your models
    Base.metadata.create_all(bind=engine)
    seed_materials()
