import unittest
import pandas as pd
from pharmatrialanalyzer.statistical_analysis import StatisticalAnalysis


class TestStatisticalAnalysis(unittest.TestCase):
    def setUp(self):
        """Set up sample data for statistical analysis."""
        self.test_data = pd.DataFrame({
            'PatientID': [1, 2, 3, 4, 5],
            'TreatmentGroup': ['Drug', 'Placebo', 'Drug', 'Placebo', 'Drug'],
            'Outcome': [1.2, 2.3, 1.5, 2.6, 1.1]
        })

    def test_t_test_analysis(self):
        """Test if the t-test analysis returns expected results."""
        analyzer = StatisticalAnalysis(self.test_data)
        result = analyzer.perform_analysis()

        # Check if the t-test result is returned
        self.assertIn('t-test', result)
        
        # Example of checking if the p-value and statistic exist
        self.assertIn('p-value', result['t-test'])
        self.assertIn('statistic', result['t-test'])
        
        # Check if p-value and statistic are of float type
        self.assertIsInstance(result['t-test']['p-value'], float)
        self.assertIsInstance(result['t-test']['statistic'], float)

    def test_anova_analysis(self):
        """Test if the ANOVA analysis returns expected results."""
        analyzer = StatisticalAnalysis(self.test_data)
        result = analyzer.perform_analysis()

        # Check if the ANOVA result is returned
        self.assertIn('anova', result)
        
        # Example of checking if the p-value and statistic exist for ANOVA
        self.assertIn('p-value', result['anova'])
        self.assertIn('statistic', result['anova'])

        # Check if the ANOVA p-value and statistic are of float type
        self.assertIsInstance(result['anova']['p-value'], float)
        self.assertIsInstance(result['anova']['statistic'], float)

    def test_no_treatment_group(self):
        """Test if the analysis raises an error when 'TreatmentGroup' is missing."""
        # Remove 'TreatmentGroup' column from test data
        invalid_data = self.test_data.drop(columns=['TreatmentGroup'])

        analyzer = StatisticalAnalysis(invalid_data)
        
        # Ensure an error is raised when the required column is missing
        with self.assertRaises(KeyError):
            analyzer.perform_analysis()


if __name__ == '__main__':
    unittest.main()
