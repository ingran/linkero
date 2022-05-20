from setuptools import setup
from linkero.core.common import Metadata

metadata = Metadata()

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """
Linkero is compatible with **Python-2** and **Python-3**.

************************************
What can I do with Linkero?
************************************

- Run REST API server
- Mount your Python developments or wrappers as API REST service. Only spend time developing your APIs behaviour.
- Add new APIs easily to already existing gateway development.
- Generate Public APIs.
- Generate Private APIs.
    - Security using user and password authentication.
    - Security using token.
    - Grant privileges to desired APIs or only a group of calls of API to specific users.
- User accounts persistence using SQLite DB.
- Integration with other WSGI (Web Server Gateway Interface):
    - Gevent_
    - Waitress_

.. _Gevent: https://github.com/gevent/gevent
.. _Waitress: https://github.com/Pylons/waitress


Installation
============

You can install or upgrade linkero with:

- ``$ pip install linkero --upgrade``

Or you can install from source with:

- ``$ git clone https://github.com/ingran/linkero.git --recursive``

- ``$ cd linkero``

- ``$ pip install .``
   """

setup(
    name = 'linkero',
    packages = ['linkero', 'linkero.core', 'linkero.core.gateway', 'linkero.config', 'linkero.tools'],
    package_data={'linkero': ['config/config.json']},
    install_requires=requirements(),
    version = metadata.get_version(),
    license = 'LGPL v3',
    description = 'Restful API for external requests',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/ingran/linkero',
    download_url = 'https://github.com/ingran/linkero/archive/v'+metadata.get_version()+'.tar.gz',
    keywords = 'framework rest-api restful-api web-services',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Programming Language :: Python :: Implementation :: PyPy'],
)
