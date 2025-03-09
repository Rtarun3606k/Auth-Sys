import secrets
import string
from datetime import datetime


def serialize_doc(doc):
    """
    Convert MongoDB document to JSON-serializable format.
    """
    if doc:
        doc['_id'] = str(doc['_id'])
    return doc



def generate_api_key(app_name: str, length: int = 32) -> str:
    """
    Generate a unique API key using the application name as input.
    
    :param app_name: The name of the application.
    :param length: The length of the generated API key (default is 32).
    :return: A unique API key string.
    """
    # Define the character set for the API key
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random string of the specified length
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    
    # Get the current timestamp without spaces
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Combine the app name, timestamp, and random string to create the API key
    api_key = f"{app_name}_{timestamp}_{random_string}"
    print(api_key)
    
    return api_key

# Example usage
