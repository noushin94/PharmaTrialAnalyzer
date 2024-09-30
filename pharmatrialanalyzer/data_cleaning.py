class DataCleaning:
    def __init__(self, data):
        self.data = data

    def clean(self):
        """Cleans the data by filling missing values and correcting data types."""
        self.data.fillna(method='ffill', inplace=True)
        self.data['Age'] = self.data['Age'].astype(int)
        # Additional cleaning steps...
        logger.info("Data cleaning completed successfully")
        return self.data
