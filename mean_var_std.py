import numpy as np

def calculate(list_input):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    for a 3x3 matrix created from a 9-element list.
    
    Args:
        list_input (list): A list containing exactly 9 numbers
        
    Returns:
        dict: A dictionary containing statistics for rows, columns, and flattened matrix
        
    Raises:
        ValueError: If the input list doesn't contain exactly 9 elements
    """
    
    # Check if the input list has exactly 9 elements
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list_input).reshape(3, 3)
    
    # Calculate statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of columns
            matrix.mean(axis=1).tolist(),  # mean of rows
            matrix.mean()                  # mean of flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of columns
            matrix.var(axis=1).tolist(),   # variance of rows
            matrix.var()                   # variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # std dev of columns
            matrix.std(axis=1).tolist(),   # std dev of rows
            matrix.std()                   # std dev of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of columns
            matrix.max(axis=1).tolist(),   # max of rows
            matrix.max()                   # max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of columns
            matrix.min(axis=1).tolist(),   # min of rows
            matrix.min()                   # min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of columns
            matrix.sum(axis=1).tolist(),   # sum of rows
            matrix.sum()                   # sum of flattened matrix
        ]
    }
    
    return calculations


# Example usage and testing
if __name__ == "__main__":
    # Test the function
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(test_list)
    
    print("Input list:", test_list)
    print("\n3x3 Matrix:")
    print(np.array(test_list).reshape(3, 3))
    print("\nCalculations:")
    
    for key, value in result.items():
        print(f"{key}:")
        print(f"  Columns: {value[0]}")
        print(f"  Rows:    {value[1]}")
        print(f"  Flattened: {value[2]}")
        print()
    
    # Test error handling
    try:
        calculate([1, 2, 3, 4, 5])  # This should raise an error
    except ValueError as e:
        print(f"Error handling test: {e}")