from setuptools import setup, find_packages

setup(
    name='PharmaTrialAnalyzer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'scipy',
        'jinja2',
        # Add other dependencies...
    ],
    entry_points={
        'console_scripts': [
            'run-analysis=pharmatrialanalyzer.main:main',
        ],
    },
    author='Noushin Ahmadvand',
    author_email='Noushin_ahmadvand@yahoo.com',
    description='A package for clinical trial data analysis in the pharmaceutical industry.',
    url='https://github.com/noushin94/PharmaTrialAnalyzer',
)
