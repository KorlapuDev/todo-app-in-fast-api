import bcrypt
import jwt
import datetime
from config.creds import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


async def jwt_creation_fun(username):
    payload: dict = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # Token expiration time set to 30 minutes
    }
    # Encode (create) the JWT
    encoded_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_token


async def password_Hash(password_to_hash):
    bytes = password_to_hash.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    bytes_passoword = bcrypt.hashpw(bytes, salt)
    return bytes_passoword


async def password_check(password_to_check, password_in_db):
    bytes = password_to_check.encode('utf-8')
    result = bcrypt.checkpw(bytes, password_in_db)
    return result
