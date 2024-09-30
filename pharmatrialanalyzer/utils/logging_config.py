import logging

logging.basicConfig(
    filename='logs/pharma_trial_analyzer.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)
