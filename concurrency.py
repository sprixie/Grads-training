import numpy as np
from statCalculator import statisticalCalculator
from concurrent.futures import ThreadPoolExecutor, as_completed

def main(data):
    calculator = statisticalCalculator(data)
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(calculator.mean): 'mean',
            executor.submit(calculator.median): 'median',
            executor.submit(calculator.sampleVariance): 'sampleVariance',
            executor.submit(calculator.standardDeviation): 'standardDeviation'
        }

        for future in as_completed(futures):
            stat_name = futures[future]
            try:
                result = future.result()
                print(f"{stat_name}: {result}")
            except Exception as e:
                print(f"Error computing {stat_name}: {e}")

# Example usage
if __name__ == "__main__":
    data = np.array([1,2,3,5])  # Replace with your data
    main(data)
