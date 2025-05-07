import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    def show_columns(self):
        print("\nColumns in the dataset:")
        for col in self.data.columns:
            print(f"- {col}")

    def plot_histogram(self, column):
        if column in self.data.columns:
            sns.histplot(self.data[column], kde=True)
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print("Column not found!")

    def plot_scatter(self, x_col, y_col):
        if x_col in self.data.columns and y_col in self.data.columns:
            sns.scatterplot(x=self.data[x_col], y=self.data[y_col])
            plt.title(f"Scatter Plot: {x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        else:
            print("One or both columns not found!")

    def plot_correlation_heatmap(self):
        numeric_data = self.data.select_dtypes(include='number')
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    def run(self):
        self.load_data()
        if self.data is not None:
            self.show_columns()
            while True:
                print("\nChoose a visualization option:")
                print("1. Histogram")
                print("2. Scatter Plot")
                print("3. Correlation Heatmap")
                print("4. Exit")
                choice = input("Enter choice (1-4): ")

                if choice == '1':
                    col = input("Enter column name for histogram: ")
                    self.plot_histogram(col)
                elif choice == '2':
                    x = input("Enter x-axis column: ")
                    y = input("Enter y-axis column: ")
                    self.plot_scatter(x, y)
                elif choice == '3':
                    self.plot_correlation_heatmap()
                elif choice == '4':
                    print("Exiting visualization tool.")
                    break
                else:
                    print("Invalid choice. Try again.")


# --- Driver Code ---
if __name__ == "__main__":
    file_path = input("Enter the path to your CSV file: ")
    visualizer = DataVisualizer(file_path)
    visualizer.run()
