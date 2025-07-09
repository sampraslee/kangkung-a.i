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
                # *** THIS LINE IS UPDATED TO MATCH THE NEW CSV COLUMN ORDER ***
                # Name, Image, Type, Vegetable ID, Description
                name, image, type_str, vegetable_ids_str, description = row

                # Clean up the data
                name = name.strip()
                image = image.strip() if image else None  # Handle empty image field
                type_str = type_str.strip().lower()
                # Handle empty description field
                description = description.strip() if description else None

                print(f"Processing material: {name}")

                # --- Core Many-to-Many Logic ---

                # 1. Find or create the Material object
                # This check prevents creating duplicate materials if you run the script again.
                material = db.query(models.Material).filter(
                    models.Material.name == name).first()
                if not material:
                    material = models.Material(
                        name=name,
                        type=type_str,
                        image=image,       # Pass the image
                        description=description  # Pass the description
                    )
                    db.add(material)
                    db.flush()  # Flush to get the material.id if it's new
                    print(f"  - Created new material: {name}")
                else:
                    # If material already exists, update its image and description
                    # You might want to update other fields too if necessary
                    material.image = image
                    material.description = description
                    material.type = type_str  # Update type as well
                    print(
                        f"  - Material '{name}' already exists. Updating image and description.")

                # Process vegetable links
                vegetable_ids = []
                if vegetable_ids_str:
                    try:
                        # Split by comma and convert to integers, handling potential spaces
                        vegetable_ids = [
                            int(v_id.strip()) for v_id in vegetable_ids_str.split(',') if v_id.strip()]
                    except ValueError:
                        print(
                            f"    - WARNING: Could not parse vegetable IDs for {name}: {vegetable_ids_str}. Skipping links.")

                # Remove existing links not present in the new list to keep data consistent
                current_veg_ids = {veg.id for veg in material.vegetables}
                for veg_id_to_remove in current_veg_ids - set(vegetable_ids):
                    vegetable_to_remove = db.query(models.Vegetable).filter(
                        models.Vegetable.id == veg_id_to_remove).first()
                    if vegetable_to_remove in material.vegetables:
                        material.vegetables.remove(vegetable_to_remove)
                        print(
                            f"    - Removing link to vegetable ID: {veg_id_to_remove} ({vegetable_to_remove.name})")

                if vegetable_ids:
                    print(
                        f"  - Linking material '{name}' to vegetables: {vegetable_ids}")
                    for veg_id in vegetable_ids:
                        vegetable = db.query(models.Vegetable).filter(
                            models.Vegetable.id == veg_id).first()

                        if vegetable:
                            # 3. Create the link
                            # Check if the link already exists before adding
                            if vegetable not in material.vegetables:
                                material.vegetables.append(vegetable)
                                print(
                                    f"    - Linking to vegetable ID: {veg_id} ({vegetable.name})"
                                )
                            else:
                                print(
                                    f"    - Link to vegetable ID: {veg_id} already exists. Skipping."
                                )
                        else:
                            print(
                                f"    - WARNING: Vegetable with ID {veg_id} not found. Skipping."
                            )

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