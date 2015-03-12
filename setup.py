from os.path import join, dirname
from setuptools import setup
from imp import load_source

description = "RetailCrm REST API client"
version = load_source("version", join("retailcrm", "version.py"))

setup(
    name='api-client-python',
    version=version.__version__,
    url='https://github.com/retailcrm/api-client-python',
    description=description,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    keywords='crm, saas, rest, e-commerce',
    license='MIT',
    author='RetailCrm',
    author_email='integration@retailcrm.ru',
    package_data={},
    install_requires=['requests']
)
