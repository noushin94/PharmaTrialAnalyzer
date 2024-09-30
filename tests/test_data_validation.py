import unittest
from pharmatrialanalyzer.data_validation import DataValidation
import pandas as pd

class TestDataValidation(unittest.TestCase):
    def test_validate_success(self):
        data = pd.DataFrame({
            'PatientID': [1, 2],
            'Age': [35, 42],
            'TreatmentGroup': ['Drug', 'Placebo'],
            'Outcome': [5.0, 3.5]
        })
        validator = DataValidation(data)
        try:
            validator.validate()
        except Exception as e:
            self.fail(f"Validation failed with exception {e}")

    def test_validate_missing_column(self):
        data = pd.DataFrame({
            'PatientID': [1, 2],
            'Age': [35, 42],
            'Outcome': [5.0, 3.5]
        })
        validator = DataValidation(data)
        with self.assertRaises(DataValidationError):
            validator.validate()
