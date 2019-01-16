import logging

from sqlalchemy import Column, String
from restalchemy.auth import PasswordMixin

from .meta import Base
from .mixins import BaseMixin

log = logging.getLogger(__name__)


class User(BaseMixin, PasswordMixin, Base):
    __json_private__ = ['password']

    email = Column(String(64), nullable=False)
    name = Column(String(64), server_default="")
