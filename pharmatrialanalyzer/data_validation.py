from utils.exceptions import DataValidationError

class DataValidation:
    def __init__(self, data):
        self.data = data

    def validate(self):
        """Validates the data according to predefined rules."""
        required_columns = ['PatientID', 'Age', 'TreatmentGroup', 'Outcome']
        for col in required_columns:
            if col not in self.data.columns:
                raise DataValidationError(f"Missing required column: {col}")

        if self.data['Age'].min() < 18:
            raise DataValidationError("Age cannot be less than 18")
        # Additional validation rules...
        logger.info("Data validation completed successfully")
