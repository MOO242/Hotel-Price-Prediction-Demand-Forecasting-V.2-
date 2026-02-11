import sys
import os
from dataclasses import dataclass
import logging
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import logger
import numpy as np
from sklearn.model_selection import train_test_split

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

load_dotenv()


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):

        self.ingestion_config = DataIngestionConfig()

        # Database credentials
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        db = os.getenv("POSTGRES_DB")

        # Connection string with autocommit for immediate saving
        self.connection_uri = f"postgresql://{user}:{password}@{host}:5432/{db}"
        self.engine = create_engine(self.connection_uri, isolation_level="AUTOCOMMIT")

    def upload_to_postgres(self):
        logging.info("--- Step 1: Loading & Cleaning Data ---")
        df = pd.read_csv("Notebook/data.csv")

        logger.info(f"--- Step 2: Uploading {len(df)} rows to 'hotel_bookings' ---")
        try:
            # Using if_exists='replace' will drop the old (wrong) table
            # and create a new one that matches these data types exactly.
            df.to_sql(
                name="hotel_bookings",
                con=self.engine,
                if_exists="replace",
                index=False,
                chunksize=1000,
                method="multi",
            )
            logger.info("Upload successful!")

            # 3. Verification check
            self.verify_upload()
            logger.info("verify successful!")

        except Exception as e:
            raise CustomException(e, sys)

    def verify_upload(self):
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM hotel_bookings"))
            count = result.scalar()
            logger.info(f"--- Step 3: Verification ---")
            logger.info(f"Rows found in PostgreSQL: {count}")

    def initiate_data_split(self):

        logger.info("--- Step 4: Initiating Train-Test Split ---")
        try:
            # 1. Pull data from the SQL table we just created
            query = "SELECT * FROM hotel_bookings"
            df = pd.read_sql_query(text(query), self.engine.connect())
            logger.info("Data read from SQL successful. Starting split...")

            # 2. Create a folder to save the splits
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # 3. Perform the split (80% Train, 20% Test)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # 4. Save to CSVs for the Training Pipeline to use
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logger.info("Train and Test sets saved to 'artifacts' folder.")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":

    ingestor = DataIngestion()
    ingestor.upload_to_postgres()

    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_split()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data
    )
