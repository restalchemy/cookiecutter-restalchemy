import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "SQLAlchemy",
    "alembic",
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_debugtoolbar",
    "pyramid_retry",
    "pyramid_tm",
    "restalchemy",
    "transaction",
    "waitress",
    "zope.sqlalchemy",
    # Needed if you use the default RESTAlchemy authentication:
    "bcrypt",
    "pyramid-jwt",
]

tests_require = ["WebTest", "pytest", "pytest-cov"]

setup(
    name="{{ cookiecutter.repo_name }}",
    version="0.0",
    description="{{ cookiecutter.api_name }}",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="rest api restalchemy sqlalchemy pyramid",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require},
    install_requires=requires,
    entry_points={
        "paste.app_factory": ["main = {{ cookiecutter.repo_name }}:main"],
        "console_scripts": [
            "initialize_{{ cookiecutter.repo_name }}_db={{ cookiecutter.repo_name }}.scripts.initialize_db:main"
        ],
    },
)
