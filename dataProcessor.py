import numpy as np
import pandas as pd
from multiprocessing import Pool, cpu_count


class dataProcessor():
    def __init__(self, file_path):
        """
        Initialize the processor with the path to the dataset.

        Parameters:
        file_path (str): The path to the CSV file containing the dataset.
        """
        self.file_path = file_path
        self.data = None

    def loadData(self):
        """
        Load the dataset from the specified file path into a DataFrame.

        Raises:
        FileNotFoundError: If the file at file_path does not exist.
        """
        self.data = pd.read_csv(self.file_path)

    def removeDuplicates(self):
        """
        Remove duplicate rows from the dataset.

        Only operates if the data has been loaded successfully.
        """
        if self.data is not None:
            self.data.drop_duplicates(inplace=True)

    def fillMissingValues(self, method='mean'):
        """
        Fill missing values in the dataset.

        Parameters:
        method (str): The method used to fill missing values. Options include:
                      'mean' - fills with the mean of the column,
                      'median' - fills with the median of the column,
                      'drop' - drops rows with missing values in the 'value' column.

        Raises:
        ValueError: If an invalid method is provided.
        """
        if self.data is not None:
            if method == 'mean':
                self.data['value'].fillna(self.data['value'].mean(), inplace=True)
            elif method == 'median':
                self.data['value'].fillna(self.data['value'].median(), inplace=True)
            elif method == 'drop':
                self.data.dropna(subset=['value'], inplace=True)
            else:
                raise ValueError("Invalid method. Options include 'mean', 'median', or 'drop'")

    def aggregateByGroup(self):
        """
        Aggregate the dataset by 'category' and calculate the mean of 'value'.

        Returns:
        DataFrame: A DataFrame containing the aggregated results.
        """
        if self.data is not None:
            return self.data.groupby('category')['value'].mean().reset_index()

    def exportCleanData(self, output_file_path):
        """
        Export the cleaned dataset to the specified file path.

        Parameters:
        output_file_path (str): The path where the cleaned dataset will be saved.

        Raises:
        ValueError: If no data has been loaded.
        """
        if self.data is not None:
            self.data.to_csv(output_file_path, index=False)
            print(f"Cleaned data saved to {output_file_path}")
        else:
            raise ValueError("No data has been loaded to export.")

    def cleanData(self, output_file_path, method='mean'):
        """
        Load, clean, and export the dataset using multiprocessing.

        Parameters:
        output_file_path (str): The path where the cleaned dataset will be saved.
        method (str): The method used to fill missing values.
        """
        self.loadData()

        with Pool(processes=cpu_count()) as pool:
            # Distributing the tasks across multiple processes
            cleaned_data = pool.apply(self.removeDuplicates, args=(self.data,))
            cleaned_data = pool.apply(self.fillMissingValues, args=(cleaned_data, method))
            aggregated_data = pool.apply(self.aggregateByGroup, args=(cleaned_data,))
        
        self.exportCleanData(output_file_path, aggregated_data)


if __name__ == "__main__":
    processor = dataProcessor(r'C:\Users\MeriemElkhal\Grads-training\large_dataset.csv')
    processor.loadData()
    aggregated_data = processor.aggregateByGroup()
    print(aggregated_data)
    processor.cleanData(r'C:\Users\MeriemElkhal\Grads-training\cleaned_dataset.csv', method='mean')
