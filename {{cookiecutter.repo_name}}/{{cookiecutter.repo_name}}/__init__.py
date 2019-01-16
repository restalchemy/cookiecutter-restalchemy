import logging
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

log = logging.getLogger(__name__)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, authorization_policy=ACLAuthorizationPolicy())
    config.include(".models")
    config.include("restalchemy")
    config.include("restalchemy.auth")
    config.set_authenticate_function("{{cookiecutter.repo_name}}.auth.authenticate")
    config.set_get_model_function("{{cookiecutter.repo_name}}.utils.get_model")
    config.scan()
    return config.make_wsgi_app()
