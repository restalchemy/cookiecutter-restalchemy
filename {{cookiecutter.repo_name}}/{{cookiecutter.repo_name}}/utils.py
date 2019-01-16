from pyramid.request import Request

from . import models


def get_model(request: Request, name: str):
    """Checks that :param:`name` is a valid model.
    Converts plural `name` to capitalized singular form
    and '-' or '_' separation to camelCase.
    Returns the model class or model name string if found, None otherwise.

    E.g.::

        >>> get_model("countries")
        <class '{{ cookiecutter.repo_name }}.models.Country'>
        >>> get_model("USER")
        <class '{{ cookiecutter.repo_name }}.models.User'>
        >>> get_model("user-language", False)
        <class '{{ cookiecutter.repo_name }}.models.UserLanguage'>
        >>> get_model("InvalidModel")
        None

    :param str name: model name to convert
    :return: model class or None
    """
    if "-" in name:
        model_name = "".join(m.capitalize() for m in name.split("-"))
    elif "_" in name:
        model_name = "".join(m.capitalize() for m in name.split("_"))
    else:
        model_name = name.capitalize()

    if model_name.endswith("ies"):  # change e.g. Countries to Countr*y*
        model_name = model_name[:-3] + "y"
    else:
        model_name = model_name.rstrip("s")

    return getattr(models, model_name, None)
