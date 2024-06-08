import pandas as pd
from sqlalchemy import create_engine, inspect, types
import os
from tqdm import tqdm

def table_exists(engine, table_name):
    insp = inspect(engine)
    return insp.has_table(table_name)

def load(path, table_name):
    try:
        csv_file = os.path.basename(path)
        print(f"\n🟠 Loading data from '{csv_file}' as '{table_name}'")

        # Create engine to connect to the PostgreSQL database
        engine = create_engine("postgresql://dgerwig:userpw@localhost:5432/piscineds")

        # Check if the table already exists
        if table_exists(engine, table_name):
            print(f"❗️ Table '{table_name}' already exists. Data not loaded.")
            return

        # Get the total number of lines in the CSV file
        total_lines = sum(1 for line in open(path))

        # Initialize progress bar
        with tqdm(total=total_lines, unit=' lines', unit_scale=True, desc="Progress") as pbar:
            # Read CSV file in chunks and load data into the database
            chunk_size = 10000  # Adjust chunk size according to your preference
            for chunk in pd.read_csv(path, encoding='latin1', chunksize=chunk_size):
                # Define data types for each column
                data_types = {
                    "event_time": types.DateTime(),
                    "event_type": types.String(length=255),
                    "product_id": types.Integer(),
                    "price": types.Float(),
                    "user_id": types.BigInteger(),
                    "user_session": types.String(length=36)  # Assuming UUIDs are stored as strings
                }
                chunk.to_sql(table_name, engine, index=False, dtype=data_types, if_exists='append')
                pbar.update(len(chunk))

        print("✅ Data loaded successfully.")

        # Dispose of the engine
        engine.dispose()

    except Exception as error:
        print(f"❌ Error: {error}")

def main():
    path = "/System/Volumes/Data/sgoinfre/goinfre/Perso/dgerwig-/Data_Science/subject/customer/data_2022_oct.csv"
    load(path, "data_2022_oct")

if __name__ == "__main__":
    main()

