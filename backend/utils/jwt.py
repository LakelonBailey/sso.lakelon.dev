from datetime import datetime, timedelta, timezone

from jwt import (
    JWT,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

instance = JWT()


def create_token(payload: dict) -> str:
    payload.update({
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(hours=2)
        )
    })

    with open('jwtRS256.key', 'rb') as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    return instance.encode(payload, signing_key, alg='RS256')
