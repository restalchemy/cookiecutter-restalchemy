from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func


def model_name_to_schema(name: str) -> str:
    """Gets a name of a :mod:`{{ cookiecutter.repo_name }}.models`
    and returns the sql schema (table name).
    E.g.::

        >>> model_name_to_schema('UserLanguage')
        'user_languages'
        >>> model_name_to_schema('User')
        'users'
        >>> model_name_to_schema('Country')
        'countries'

    :param str name: Name of the model to convert
    :return: :class:`str` sql table name
    """
    schema = name[0]
    for i in range(1, len(name)):
        if name[i].isupper():
            schema += "_"
        schema += name[i]

    schema = schema.lower()
    if schema.endswith("y"):  # change e.g. Country to countr*ies*
        schema = schema[:-1] + "ies"

    return schema.rstrip("s") + "s"


class TimestampMixin:
    """Add created_at and updated_at columns."""

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class BaseMixin(TimestampMixin):
    """Add tablename attribute, id, created_at and updated_at columns."""

    @declared_attr
    def __tablename__(cls):
        return model_name_to_schema(cls.__name__)

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = []
        for a in ["id", "uid", "name", "nick", "email", "code"]:
            if hasattr(self, a):
                attrs.append(f"{a}={getattr(self, a)}")
        attrs = ", ".join(attrs)
        return f"{class_name}({attrs})"
