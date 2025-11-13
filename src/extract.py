import requests
import pandas as pd
from src.config import API_URL

def extract_breweries() -> pd.DataFrame:
    """Extract brewery data from the Open Brewery DB API and return a Pandas Dataframe."""
    print("Extracting data from API...")

    #Calling the API
    response = requests.get(API_URL, timeout=10)

    #If the status code is not 200 (OK), this will raise an error and stop. 
    response.raise_for_status()

    #Convert the JSON response into Python Object(List/Dict)
    data = response.json()

    #Turn that into a DataFrame
    df = pd.DataFrame(data)

    print(f"Extracted {len(df)} rows")
    return df