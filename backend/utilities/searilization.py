import secrets
import string
import datetime


def serialize_doc(doc):
    """
    Convert MongoDB document to JSON-serializable format.
    """
    if doc:
        doc['_id'] = str(doc['_id'])
    return doc



def generate_api_keys(app_name: str) -> dict:
    """
    Generate unique API keys using the application name as input.
    
    :param app_name: The name of the application.
    :return: A dictionary containing the generated API keys.
    """
    def generate_key(suffix: str, length: int = 32) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        random_string = ''.join(secrets.choice(characters) for _ in range(length))
        timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        api_key = f"{app_name}_{suffix}_{timestamp}_{random_string}"
        return api_key

    api_keys = {
        'apiKey1': generate_key('key1'),
        'apiKey2': generate_key('key2')
    }
    return api_keys