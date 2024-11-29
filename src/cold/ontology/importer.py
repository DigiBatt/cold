import requests


def import_ontology_turtle(url, local_file_path):
    """
    Downloads a Turtle file from a given URL and saves it locally.

    Args:
        url (str): The URL to the Turtle file.
        local_file_path (str): The path to save the local Turtle file.

    Returns:
        None
    """
    try:
        # Send a GET request to fetch the content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        print("path = ", local_file_path)
        # Write the content to the local file
        with open(local_file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Turtle file successfully saved to: {local_file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the Turtle file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
