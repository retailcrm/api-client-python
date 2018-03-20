# coding=utf-8

"""
Setup file
"""

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='retailcrm',
    version='5.0.0',
    description='retailCRM multi version API client',
    long_description=read('README.md'),
    url='https://github.com/retailcrm/api-client-python',
    author='retailCRM',
    author_email='integration@retailcrm.ru',
    keywords='crm, saas, rest, e-commerce',
    license='MIT',
    packages=['retailcrm', 'tests'],
    package_data={},
    install_requires=['requests', 'multidimensional_urlencode', 'nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
