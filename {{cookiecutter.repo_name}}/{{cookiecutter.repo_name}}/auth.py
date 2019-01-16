from pyramid.request import Request

from .models import User


def authenticate(request: Request):
    email = request.data.get("email")
    password = request.data.get("password")

    user: User = request.dbsession.query(User).filter(User.email == email).one()

    if user and user.password_verify(password):
        expiration = 3600  # Auth token is valid for 1 hour
        return user.id, expiration, user._password_counter
