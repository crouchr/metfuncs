# see - https://packaging.python.org/guides/hosting-your-own-index/
# run '$ pipenv run python setup.py bdist_wheel' to create a WHeel file

from setuptools import setup, find_packages

setup(version='1.0.7',
      description='Functions for handling meteorological data',
      author='Richard Crouch',
      author_email='richard.crouch100@gmail.com',
      license='MIT',
      include_package_data=True,
      py_modules=['metfuncs', 'windrose'],
      zip_safe=False
      )
