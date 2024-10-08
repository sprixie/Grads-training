def quicksort(arr):
    """Implementation of the quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def calculateSMA(data, windowSize):
    """Calculate the Simple Moving Average (SMA) of a time series."""
    if not data:
        raise ValueError("Input data cannot be empty.")
    if windowSize <= 0:
        raise ValueError("Window size must be greater than 0.")
    if windowSize > len(data):
        raise ValueError("Window size cannot be greater than the length of the data.")

    sma = []
    for i in range(len(data) - windowSize + 1):
        window = data[i:i + windowSize]
        windowAverage = sum(window) / windowSize
        sma.append(windowAverage)

    return sma

def calculateEMA(data, windowSize):
    """Calculate the Exponential Moving Average (EMA) of a time series."""
    if not data:
        raise ValueError("Input data cannot be empty.")
    if windowSize <= 0:
        raise ValueError("Window size must be greater than 0.")
    if windowSize > len(data):
        raise ValueError("Window size cannot be greater than the length of the data.")

    ema = []
    k = 2 / (windowSize + 1)  # Smoothing factor

    # Start with the first data point as the initial EMA
    ema.append(data[0])

    for price in data[1:]:
        newEMA = (price - ema[-1]) * k + ema[-1]
        ema.append(newEMA)

    # Return EMA truncated to the size of original data
    return ema