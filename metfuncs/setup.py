# see - https://packaging.python.org/guides/hosting-your-own-index/
# run '$ pipenv run python setup.py bdist_wheel' to create a Wheel file

from setuptools import setup, find_packages

setup(version='1.0.22',
      description='Functions for handling meteorological data',
      author='Richard Crouch',
      author_email='richard.crouch100@gmail.com',
      license='MIT',
      include_package_data=True,
      zip_safe=False,
      py_modules=[
            'metfuncs',
            'windrose',
            'solar_funcs',
            'solar_rad_expected',
            'wind_calibration',
            'okta_funcs',
            'feels_like',
            'wet_bulb',
            'fog',
            'synopsis'
            ],
      )
