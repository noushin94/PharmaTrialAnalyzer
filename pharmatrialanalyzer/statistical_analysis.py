from scipy import stats

class StatisticalAnalysis:
    def __init__(self, data):
        self.data = data

    def perform_analysis(self):
        """Performs statistical analysis on the data."""
        treatment_group = self.data[self.data['TreatmentGroup'] == 'Drug']
        control_group = self.data[self.data['TreatmentGroup'] == 'Placebo']
        result = stats.ttest_ind(treatment_group['Outcome'], control_group['Outcome'])
        logger.info("Statistical analysis completed")
        return result
