from distutils.core import setup
from linkero import Metadata

metadata = Metadata()

long_description = """
Restful API for external requests
   """

setup(
    name = 'linkero',
    packages = ['linkero', 'linkero.core', 'linkero.core.gateway', 'linkero.config', 'linkero.tools'],
    package_data={'linkero': ['config/config.json']},
    version = metadata.get_version(),
    license = 'AGPL v3',
    description = 'Restful API for external requests',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/ingran/linkero',
    download_url = 'https://github.com/ingran/linkero/archive/v'+metadata.get_version()+'.tar.gz',
    keywords = ['framework', 'rest-api', 'restful-api', 'web-services'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)