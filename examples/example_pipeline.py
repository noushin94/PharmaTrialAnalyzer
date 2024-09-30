from pharmatrialanalyzer.data_ingestion import DataIngestion
from pharmatrialanalyzer.data_validation import DataValidation
from pharmatrialanalyzer.data_cleaning import DataCleaning
from pharmatrialanalyzer.statistical_analysis import StatisticalAnalysis
from pharmatrialanalyzer.visualization import Visualization
from pharmatrialanalyzer.report_generation import ReportGenerator
from pharmatrialanalyzer.utils.logging_config import logger


def run_pipeline(data_source):
    logger.info("Starting PharmaTrialAnalyzer Pipeline...")

    # Step 1: Data Ingestion
    logger.info("Ingesting data...")
    ingestion = DataIngestion(data_source)
    data = ingestion.load_data()
    logger.info("Data ingestion completed.")

    # Step 2: Data Validation
    logger.info("Validating data...")
    validator = DataValidation(data)
    validator.validate()
    logger.info("Data validation completed.")

    # Step 3: Data Cleaning
    logger.info("Cleaning data...")
    cleaner = DataCleaning(data)
    cleaned_data = cleaner.clean()
    logger.info("Data cleaning completed.")

    # Step 4: Statistical Analysis
    logger.info("Performing statistical analysis...")
    analyzer = StatisticalAnalysis(cleaned_data)
    analysis_results = analyzer.perform_analysis()
    logger.info("Statistical analysis completed.")

    # Step 5: Visualization
    logger.info("Generating visualizations...")
    visualizer = Visualization(cleaned_data)
    visual_paths = visualizer.create_plots()
    logger.info("Visualizations generated.")

    # Step 6: Report Generation
    logger.info("Generating report...")
    reporter = ReportGenerator(analysis_results, visual_paths)
    reporter.generate_pdf_report()
    logger.info("Report generation completed.")

    logger.info("PharmaTrialAnalyzer Pipeline completed successfully.")


if __name__ == "__main__":
    # Path to the clinical trial data
    data_source = 'data/clinical_trial_data.csv'

    # Run the pipeline
    run_pipeline(data_source)
