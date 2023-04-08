# When performing a release:
# - increment version number in setup.py
# - run this script
# - reboot the web-server Vagrant machine or vagrant up --provision
# - check package at http://192.168.1.102/python-packages/metfuncs/
# - update the calling project's Pipfile

pipenv run python setup.py bdist_wheel
pipenv run python setup.py sdist
cp dist/* /home/crouchr/PycharmProjects/learnage/environments/production/web-server/apache/python-packages/metfuncs/
