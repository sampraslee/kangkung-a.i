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
vegetable_data = pandas.read_csv("Material Test Database.csv")
# select only columns we want to use
selected_vegetable_data = vegetable_data[
    [
        "Name",
        "Image",
        "Type",
        "Vegetable ID",
    ]
]
# take the data from those columns and use .to_sql to
selected_vegetable_data.to_sql(
    # name of the table in our database
    name="materials",
    # how we establish connection to our database
    con=engine,
    # no need to provide index as we already provided in the csv file
    index=False,
    if_exists="append",
)
