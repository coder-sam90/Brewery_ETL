# Brewery ETL Pipeline - By Sam Merrell
A beginner friendly **end-to-end ETL pipeline** that extracts brewery data from the Open Brewery API (https://www.openbrewerydb.org/), and transforms it with Python and Pandas. It then loads it into an sqlite database for analysis. In this case, I used SQLite Browser.

---

##  What this project does

**ETL Flow:**

> Open Brewery DB API → Python (requests + pandas) → Cleaned DataFrame → SQLite (`breweries.db`)

1. **Extract**
   - Calls the Open Brewery DB API
   - Pulls a page of brewery data (`per_page=50`)
   - Converts JSON → Pandas DataFrame

2. **Transform**
   - Selects only useful columns
   - Renames fields (e.g. `brewery_type → type`, `website_url → website`)
   - Handles missing websites
   - Converts `latitude` / `longitude` to numeric
   - Drops duplicate brewery IDs

3. **Load**
   - Writes the cleaned data to a **SQLite** database:
     - File: `data/breweries.db`
     - Table: `breweries`
   - Overwrites the table on each run (idempotent reload)

---

## Tech Stack

- **Language:** Python 3.x  
- **Libraries:**
  - `requests` – API calls
  - `pandas` – data cleaning & transformation
  - `SQLAlchemy` – database connection management
- **Database:** SQLite (`data/breweries.db`)
- **Tools:** Git, VS Code, DB Browser for SQLite / SQLite Viewer

---

## Project Structure

```text
brewery_etl/
├─ main.py                # Orchestrates the full ETL pipeline
├─ requirements.txt       # Python dependencies
├─ .gitignore             # Ignore venv, db files, caches, etc.
├─ README.md
├─ data/
│   └─ breweries.db       # SQLite database (created by the pipeline, gitignored)
└─ src/
    ├─ __init__.py
    ├─ config.py          # API URL + DB connection string
    ├─ extract.py         # Extract step: API → raw DataFrame
    ├─ transform.py       # Transform step: clean/shape the DataFrame
    └─ load.py            # Load step: DataFrame → SQLite


HOW IT WORKS!

In the src/config.py, we tell it the URL for the API which was the open brewery api and we set it to return 50. This was just a small project so I wanted it manageble. 
We then told it where the db connection was going to be. In this case, it was in data/breweries.db.

For transforming the data, I needed a way to keep the columns we actually wanted. 
We only keep id, name, brewery_type city, state, etc... 
I also wanted to make sure if there were any duplicates to just drop those. 

When it came down to loading the data, I used sqlalchemy engine by using the database connection from the transform stage. With utilizing pandas, I was able to use dataframs to display the cleaned data. I also wanted it to do a full clean and reload each time so I had it set to if_exists="replace" which will pull new each run. 

POSSIBLE IMPROVMENTS TO THE PROJECT:

- Adding in pagnation
- Adding in timestamps
- Adding in Postgres functions
- Potentially using grafana for a dashboard view with this db

