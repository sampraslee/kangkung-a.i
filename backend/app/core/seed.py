from sqlalchemy import (
    create_engine,
    Column,
    String,
    Text,
    Integer,
    Interval,
)
from sqlalchemy.dialects.postgresql import INTERVAL
from config import DATABASE_URL

# from sqlalchemy.orm import sessionmaker, declarative_base
import pandas

engine = create_engine(DATABASE_URL)

vegetable_data = pandas.read_csv("Vegetable Test Database.csv")

selected_vegetable_data = vegetable_data[
    [
        "Name",
        "Image",
        "Estimated Harvest Time",
        "Watering Frequency",
        "Amount of Sunlight",
        "Planting Instructions",
    ]
]

print(selected_vegetable_data)

selected_vegetable_data.to_sql(
    name="vegetables",
    con=engine,
    index=False,
    if_exists="append",
    dtype={"Watering Frequency": Interval(), "Estimated Harvest Time": Interval()},
)
