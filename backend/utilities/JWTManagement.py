import jwt
import datetime

SECRET_KEY = "pesUniversity"  # Use a strong secret key

def create_jwt(payload: dict, expires_in: int = 3600) -> str:
    """
    Create a JWT with the given payload and expiration time.
    
    :param payload: The payload to include in the JWT.
    :param expires_in: The expiration time in seconds (default is 1 hour).
    :return: The encoded JWT as a string.
    """
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt(token: str) -> dict:
    """
    Verify the given JWT and return the decoded payload.
    
    :param token: The JWT to verify.
    :return: The decoded payload.
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
    

def middleWare(authToken: str):
    """
    Middleware to verify the JWT token.
    
    :param authToken: The JWT token.
    :return: The decoded payload.
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        payload = verify_jwt(authToken)
        return payload
    except Exception as e:
        raise Exception(str(e))