from src.extract import extract_breweries
from src.transform import transform_breweries
from src.load import load_breweries


def run_pipeline():
    print("=== Brewery ETL Pipeline Starting ===")

    # Extract
    df_raw = extract_breweries()

    # Transform
    df_clean = transform_breweries(df_raw)

    # Load
    load_breweries(df_clean)

    print("=== Brewery ETL Pipeline Finished ===")


if __name__ == "__main__":
    run_pipeline()
