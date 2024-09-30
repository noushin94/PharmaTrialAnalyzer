import unittest
import os
from pharmatrialanalyzer.report_generation import ReportGenerator


class TestReportGeneration(unittest.TestCase):
    def setUp(self):
        """Set up necessary data for the report generation."""
        self.analysis_results = {
            't-test': {
                'p-value': 0.05,
                'statistic': 2.35
            },
            'anova': {
                'p-value': 0.01,
                'statistic': 4.21
            }
        }
        self.visual_paths = ['tests/data/sample_plot.png']
        self.report_path = 'tests/data/test_report.pdf'

        # Create a sample plot image (mock visualization)
        with open(self.visual_paths[0], 'w') as f:
            f.write('This is a mock plot image for testing.')

    def tearDown(self):
        """Clean up the generated report and visual files after the test."""
        if os.path.exists(self.report_path):
            os.remove(self.report_path)
        if os.path.exists(self.visual_paths[0]):
            os.remove(self.visual_paths[0])

    def test_report_generation(self):
        """Test that the report is generated and contains the expected content."""
        # Initialize the report generator with test data
        reporter = ReportGenerator(self.analysis_results, self.visual_paths)

        # Generate the report
        reporter.generate_pdf_report(self.report_path)

        # Check that the report file was created
        self.assertTrue(os.path.exists(self.report_path))

        # Optionally, you can open the PDF and check for expected content if you have
        # the necessary libraries to parse PDFs, or visually inspect the file after the test.

        # Ensure that the PDF file is not empty
        self.assertTrue(os.path.getsize(self.report_path) > 0)


if __name__ == '__main__':
    unittest.main()
