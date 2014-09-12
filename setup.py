from os.path import join, dirname

from setuptools import setup


setup(
	name='api-client-python',
	version=0.1,
	long_description=open(join(dirname(__file__), 'README.md')).read(),
	author='Intarocrm',
	package_data={},
	install_requires=[u'requests', ],
	url='https://github.com/intarocrm/api-client-python.git'
)