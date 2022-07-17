from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth

import models

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Token')  # scheme is like a domain where it applies, in this case its Token
auth = MultiAuth(token_auth,
                 basic_auth)  # multi auth can take any number of auth types but it looks at the first thing,


# and then the next


@basic_auth.verify_password
def verify_password(email_or_username, password):
    try:
        user = models.User.get(
            (models.User.email == email_or_username) |
            (models.User.username == email_or_username)
        )
        if not user.verify_password(password):
            return False
    except models.User.DoesNotExist:
        return False
    else:
        g.user = user
        return True


# tell the token auth how to verify a token

@token_auth.verify_token
def verify_token(token):
    user = models.User.verify_auth_token(token)
    if user is not None:
        g.user = user
        return True
    return False
