# 🚀 **PharmaTrialAnalyzer** 

![PharmaTrialAnalyzer Logo](https://media.rxbenefits.com/2021/09/09153604/Using-Data-to-Improve-Pharma-Ben-Mgt-Header.jpg) <!-- Add your logo or banner here -->

## 📋 Overview

**PharmaTrialAnalyzer** is a Python package designed to streamline the management and analysis of clinical trial data. The package automates the process of **ingesting**, **cleaning**, **validating**, **analyzing**, and **reporting** clinical trial data. It's built for **pharmaceutical companies**, **clinical researchers**, and **data scientists** who need to handle large datasets from clinical trials.

### 🛠️ Key Features:
- ✅ **Data ingestion** from multiple formats (CSV, Excel).
- 🛡️ **Data validation** to ensure regulatory compliance.
- 🧼 **Data cleaning** for handling missing values and standardizing formats.
- 📊 **Statistical analysis**, including **t-tests** and **ANOVA**, to assess drug efficacy.
- 📝 **Report generation** with **visualizations** for easy interpretation.

---

## 🎯 Features

- **Flexible Data Ingestion**: Load data from CSV, Excel, or SQL sources.
- **Data Validation**: Ensure clinical trial data meets key regulatory standards.
- **Data Cleaning**: Standardize data types and handle missing/corrupt entries.
- **Statistical Analysis**: Perform t-tests, ANOVA, and other statistical methods to analyze treatment outcomes.
- **Report Generation**: Create detailed PDF reports with statistical results and visualizations.


---

## 🖥️ Installation

### Prerequisites

- 🐍 Python 3.7+
- 📦 pip

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/noushin94/PharmaTrialAnalyzer.git
   cd PharmaTrialAnalyzer

⚙️ Usage

PharmaTrialAnalyzer is modular, so it can be used in parts or as a whole pipeline. You can use it in your Python scripts, Jupyter notebooks, or integrated into your existing data workflows.

Running the Example Pipeline 🏃‍♀️
Place your dataset in the data/ directory or update the path in examples/example_pipeline.py.
Run the example pipeline:
bash
Copy code
python examples/example_pipeline.py
This will:

Ingest clinical trial data.
Clean and validate the data.
Perform statistical analysis.
Generate a detailed PDF report with visualizations.
Customizing the Pipeline ✍️
Modify the pipeline by adjusting the data source, statistical methods, or output formats in the configuration file pharmatrialanalyzer/config/settings.py.

🏗️ Pipeline Overview

The PharmaTrialAnalyzer pipeline follows these steps:

🗂️ Data Ingestion: Load clinical trial data from CSV or Excel files.
✅ Data Validation: Ensure that the data meets clinical and regulatory standards.
🧼 Data Cleaning: Handle missing or inconsistent values.
📊 Statistical Analysis: Perform statistical tests (t-tests, ANOVA) to assess drug efficacy.
📈 Visualization: Generate visualizations to showcase trends and outcomes.
📝 Report Generation: Create a comprehensive report with analysis results and charts.
🧰 Modules Overview

1. Data Ingestion (data_ingestion.py)
Purpose: Load data from CSV, Excel, or other formats.
Example:
python
Copy code
from pharmatrialanalyzer.data_ingestion import DataIngestion
ingestor = DataIngestion('data/clinical_trial_data.csv')
data = ingestor.load_data()
2. Data Validation (data_validation.py)
Purpose: Validate that the dataset conforms to expected standards.
Example:
python
Copy code
from pharmatrialanalyzer.data_validation import DataValidation
validator = DataValidation(data)
validator.validate()
3. Data Cleaning (data_cleaning.py)
Purpose: Clean the dataset by handling missing values and correcting data types.
Example:
python
Copy code
from pharmatrialanalyzer.data_cleaning import DataCleaning
cleaner = DataCleaning(data)
cleaned_data = cleaner.clean()
4. Statistical Analysis (statistical_analysis.py)
Purpose: Perform statistical analysis (t-test, ANOVA) on the clinical trial data.
Example:
python
Copy code
from pharmatrialanalyzer.statistical_analysis import StatisticalAnalysis
analyzer = StatisticalAnalysis(cleaned_data)
results = analyzer.perform_analysis()
5. Visualization (visualization.py)
Purpose: Generate visualizations of the trial data.
Example:
python
Copy code
from pharmatrialanalyzer.visualization import Visualization
visualizer = Visualization(cleaned_data)
visualizer.create_plots()
6. Report Generation (report_generation.py)
Purpose: Generate PDF reports with visualizations and statistical results.
Example:
python
Copy code
from pharmatrialanalyzer.report_generation import ReportGenerator
reporter = ReportGenerator(results, visual_paths)
reporter.generate_pdf_report()
🧪 Running Tests

The PharmaTrialAnalyzer package includes a suite of unit tests to ensure each module functions as expected.

Running the Tests
Install pytest if it's not already installed:
bash
Copy code
pip install pytest
Run the tests:
bash
Copy code
pytest
This will execute all tests in the tests/ folder.

🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your branch.
Submit a pull request with a detailed description of your changes.
Please ensure your code follows PEP 8 standards and includes appropriate unit tests.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

