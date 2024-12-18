from tabulate import tabulate

def display_table(data, headers=None):
    """
    Display a table using the tabulate library.
    - data: List of dictionaries containing the data to display.
    - headers: If provided, a dictionary mapping column headers to keys, or "keys".
    """
    # Print the formatted table
    if headers == "keys" or headers is None:
        print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        print(tabulate(data, headers=headers, tablefmt="grid"))
