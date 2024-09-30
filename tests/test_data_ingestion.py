import unittest
import pandas as pd
from pharmatrialanalyzer.data_ingestion import DataIngestion
from pharmatrialanalyzer.utils.exceptions import DataIngestionError


class TestDataIngestion(unittest.TestCase):
    def setUp(self):
        """Set up paths for test files and create mock data."""
        self.valid_csv_path = 'tests/data/test_clinical_data.csv'
        self.invalid_csv_path = 'tests/data/invalid_file.csv'
        self.valid_excel_path = 'tests/data/test_clinical_data.xlsx'

        # Create test data as a CSV
        self.test_data = pd.DataFrame({
            'PatientID': [1, 2, 3],
            'Age': [34, 28, 45],
            'TreatmentGroup': ['Drug', 'Placebo', 'Drug'],
            'Outcome': [1.2, 2.3, 1.5]
        })

        # Write the test data to a CSV file and an Excel file
        self.test_data.to_csv(self.valid_csv_path, index=False)
        self.test_data.to_excel(self.valid_excel_path, index=False)

    def tearDown(self):
        """Clean up test files."""
        import os
        if os.path.exists(self.valid_csv_path):
            os.remove(self.valid_csv_path)
        if os.path.exists(self.valid_excel_path):
            os.remove(self.valid_excel_path)

    def test_load_data_csv(self):
        """Test that the DataIngestion class correctly loads CSV data."""
        ingestion = DataIngestion(self.valid_csv_path)
        data = ingestion.load_data()
        pd.testing.assert_frame_equal(data, self.test_data)

    def test_load_data_excel(self):
        """Test that the DataIngestion class correctly loads Excel data."""
        ingestion = DataIngestion(self.valid_excel_path)
        data = ingestion.load_data()
        pd.testing.assert_frame_equal(data, self.test_data)

    def test_invalid_file(self):
        """Test that the DataIngestion class raises an error for an invalid file."""
        ingestion = DataIngestion(self.invalid_csv_path)
        with self.assertRaises(DataIngestionError):
            ingestion.load_data()


if __name__ == '__main__':
    unittest.main()
