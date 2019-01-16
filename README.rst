========================
cookiecutter-restalchemy
========================

A Cookiecutter (project template) for creating a RESTAlchemy project.

This cookiecutter is derived from the official `pyramid-cookiecutter-starter template <https://github.com/Pylons/pyramid-cookiecutter-starter>`_.


Requirements
------------

* Python 3.6+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Versions
--------

This cookiecutter has several branches to support new features in Pyramid or
avoid incompatibilities.

* ``latest`` aligns with the latest stable release of RESTAlchemy, and is the
  default branch on GitHub.
* ``master`` aligns with the ``master`` branch of RESTAlchemy, and is where
  development takes place.
* ``x.y-branch`` aligns with the ``x.y-branch`` branch of RESTAlchemy.


Usage
-----

1. Generate a RESTAlchemy project, following the prompts from the command.

   .. code-block:: bash

       $ cookiecutter gh:Pylons/pyramid-cookiecutter-starter

   Optionally append a specific branch checkout to the command:

   .. code-block:: bash

       $ cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout master

2. Finish configuring the project by creating a virtual environment and
   installing your new project. These steps are output as part of the
   cookiecutter command above and are slightly different for Windows.

   .. code-block:: bash

       # Change directory into your newly created project.
       $ cd myproj
       # Create a virtual environment...
       $ python3 -m venv env
       # ...where we upgrade packaging tools...
       $ env/bin/pip install --upgrade pip setuptools
       # ...and into which we install our project and its testing requirements.
       $ env/bin/pip install -e ".[testing]"

3. Migrate the database using Alembic.

   .. code-block:: bash

      # Generate your first revision.
      $ alembic -c development.ini revision --autogenerate -m "init"
      # Upgrade to that revision.
      $ alembic -c development.ini upgrade head
      # Load default data.
      $ env/bin/initialize_*PROJECT*_db development.ini

4. Run your project's tests.

   .. code-block:: bash

       $ env/bin/pytest

5. Run your project.

   .. code-block:: bash

       $ env/bin/pserve development.ini
