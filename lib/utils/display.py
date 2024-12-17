from tabulate import tabulate

def display_table(data, headers):
    """
    Display a table using the tabulate library.
    - data: List of dictionaries containing the data to display.
    - headers: List of column names.
    """
    # Validate headers and data
    if not isinstance(headers, list):
        raise ValueError("Headers must be a list of strings.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Data must be a list of dictionaries.")

    # Validate that all dictionaries have keys matching the headers
    for item in data:
        if not all(key in item for key in headers):
            raise ValueError(f"Data item keys do not match headers: {item}")

    # Display the table
    print(tabulate(data, headers=headers, tablefmt="grid"))

