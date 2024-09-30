# pharmatrialanalyzer/__init__.py

# Import important classes and functions to make them available at the package level
from .data_ingestion import DataIngestion
from .data_validation import DataValidation
from .data_cleaning import DataCleaning
from .statistical_analysis import StatisticalAnalysis
from .report_generation import ReportGenerator
from .visualization import Visualization

# Initialize the logger for the package
from .utils.logging_config import logger

__all__ = [
    "DataIngestion",
    "DataValidation",
    "DataCleaning",
    "StatisticalAnalysis",
    "ReportGenerator",
    "Visualization"
]

# Initialize any other package-level configuration or settings
logger.info("PharmaTrialAnalyzer package initialized")
