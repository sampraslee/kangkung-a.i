from sqlalchemy import (
    create_engine,
    Interval,
)
from sqlalchemy.dialects.postgresql import INTERVAL
from config import DATABASE_URL
import pandas

# establish connection to our database
engine = create_engine(DATABASE_URL)
# read the csv file provided
vegetable_data = pandas.read_csv("Vegetable Test Database.csv")
# select only columns we want to use
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
# take the data from those columns and use .to_sql to
selected_vegetable_data.to_sql(
    # name of the table in our database
    name="vegetables",
    # how we establish connection to our database
    con=engine,
    # no need to provide index as we already provided in the csv file
    index=False,
    if_exists="append",
    # if table called 'vegetables' already exists, just add the data to existing 'vegetables' table
    dtype={"Watering Frequency": Interval(), "Estimated Harvest Time": Interval()},
)
