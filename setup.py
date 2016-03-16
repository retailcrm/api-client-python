# coding=utf-8
from setuptools import setup

setup(
    name='retailcrm',
    version='3.0.5',
    description='Client for retailCRM API',
    url='https://github.com/retailcrm/api-client-python',
    author='retailCRM',
    author_email='integration@retailcrm.ru',
    keywords='crm, saas, rest, e-commerce',
    license='MIT',
    packages=['retailcrm'],
    package_data={},
    install_requires=['requests']
)
