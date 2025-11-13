from sqlalchemy import create_engine
import pandas as pd
from src.config import DB_CONNECTION_STRING


def load_breweries(df: pd.DataFrame) -> None: 
    """Load the cleaned brewery data into the db. """
    print("Loading the data into the database....")

    #Creat the database engine
    engine = create_engine(DB_CONNECTION_STRING)

    #Use a transaction so its all or zero.
    with engine.begin() as conn: 
        df.to_sql(
            "breweries",
            con=conn,
            if_exists="replace", #overwrite table on each run
            index=False,
        )
    print("Load complete: ")