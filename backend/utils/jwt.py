from datetime import datetime, timedelta, timezone

from jwt import (
    JWT,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

instance = JWT()


def create_id_token(payload: dict) -> str:
    """
    Creates an id token signed with the private key.

    :param payload: The payload of data
    :return: A signed id token.
    """

    payload.update({
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(hours=2)
        )
    })

    with open('jwtRS256.key', 'rb') as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    return instance.encode(payload, signing_key, alg='RS256')


def create_access_token(audience, subject):
    """
    Creates an access token signed with the private key.

    :param audience: The audience (aud) claim identifies the recipients that \
        the JWT is intended for.
    :param subject: The subject (sub) claim identifies the principal that is \
          the subject of the JWT.
    :return: A signed access token.
    """

    # Define the payload for the access token
    payload = {
        'iss': 'https://sso.lakelon.dev',
        'sub': subject,
        'aud': audience,
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(hours=2)
        ),
    }

    # Load the private key for signing the access token
    with open('jwtRS256.key', 'rb') as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    # Encode and sign the access token
    access_token = instance.encode(payload, signing_key, alg='RS256')

    return access_token
