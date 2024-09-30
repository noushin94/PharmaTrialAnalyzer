import pandas as pd
from utils.logging_config import logger
from utils.exceptions import DataIngestionError

class DataIngestion:
    def __init__(self, source):
        self.source = source

    def load_data(self):
        """Loads data from the specified source."""
        try:
            if self.source.endswith('.csv'):
                data = pd.read_csv(self.source)
            elif self.source.endswith('.xlsx'):
                data = pd.read_excel(self.source)
            else:
                raise DataIngestionError("Unsupported file format")
            logger.info(f"Data loaded successfully from {self.source}")
            return data
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise DataIngestionError(f"Failed to load data: {e}")

