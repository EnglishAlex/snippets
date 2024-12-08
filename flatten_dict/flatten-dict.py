def flatten_dict(d, parent_key='', separator='.'):
    """
    Flattens a nested dictionary into a single dictionary with dot notation keys.

    Args:
        d (dict): The input dictionary (can contain nested dictionaries and lists).
        parent_key (str): The base key for recursion, used for dot notation.
        separator (str): The separator between keys in the flattened dictionary.

    Returns:
        dict: The flattened dictionary.
    """
    flattened = {}

    for k, v in d.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            # Recursive call for nested dictionaries
            flattened.update(flatten_dict(v, new_key, separator))
        elif isinstance(v, list):
            # Process each item in the list
            for i, item in enumerate(v):
                flattened.update(flatten_dict({f"{i}": item}, new_key, separator))
        else:
            # Add the final key-value pair
            flattened[new_key] = v

    return flattened

# Example usage
nested_dict = {
    "employees": [
        {
            "id": 1,
            "name": "John Doe",
            "department": "Sales",
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345"
            }
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "department": "Marketing",
            "address": {
                "street": "456 Elm St",
                "city": "Othertown",
                "state": "NY",
                "zip": "67890"
            }
        }
    ]
}

# Flatten the dictionary
flattened = flatten_dict(nested_dict)

# Print each top-level element on a new line
for key, value in flattened.items():
    print(f"{key}: {value}")
