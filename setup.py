# coding=utf-8

"""
Setup file
"""

import os
from setuptools import setup


def read(filename):
    """Read readme for long description"""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='retailcrm',
    version='5.1.2',
    description='RetailCRM API client',
    long_description=read('README'),
    url='https://github.com/retailcrm/api-client-python',
    author='RetailCRM',
    author_email='support@retailcrm.pro',
    keywords='crm saas rest e-commerce',
    license='MIT',
    packages=['retailcrm', 'retailcrm/versions'],
    package_data={},
    install_requires=['requests', 'multidimensional_urlencode', 'nose', 'coverage', 'pook', 'setuptools'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
