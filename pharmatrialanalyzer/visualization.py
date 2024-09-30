import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, data):
        self.data = data

    def create_plots(self):
        """Creates visualizations for the report."""
        plt.figure(figsize=(10, 6))
        self.data.groupby('VisitDate')['Outcome'].mean().plot()
        plt.title('Average Outcome Over Time')
        plt.savefig('visuals/average_outcome.png')
        logger.info("Visualizations created successfully")
        return ['visuals/average_outcome.png']
