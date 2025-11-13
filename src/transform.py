import pandas as pd

def transform_breweries(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize brewery data."""
    print("Transforming data...")

    # Keep only the columns we want (and that actually exist)
    cols = [
        "id",
        "name",
        "brewery_type",
        "city",
        "state",
        "country",
        "longitude",
        "latitude",
        "website_url",
        # "updated_at",  # removed because the API doesn't return this
    ]
    df = df[cols].copy()

    # Rename columns for easier use later
    df = df.rename(columns={
        "brewery_type": "type",
        "website_url": "website",
    })

    # Fill missing website entries
    df["website"] = df["website"].fillna("")

    # Convert coordinates to floats
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")

    # Remove duplicate breweries
    df = df.drop_duplicates(subset=["id"])

    print(f"Transform complete: {len(df)} rows, {len(df.columns)} columns.")
    return df
