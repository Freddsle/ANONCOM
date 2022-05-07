# ANONCOM
ANONCOM for IB.

ANONCOM (ANONimous COMplaints) is a site created as a training task for the Python programming course. The aim of the project is to create a space where students of Bioinformatics Institute can share their ideas and opinions.

# Install

## Install and run with pip (Ubuntu)
```console
git clone https://github.com/Freddsle/ANONCOM
cd ANONCOM/

# Create and activate your virtual environment

# Install venv
sudo apt install python3-venv

# create virtual environment (with python 3.9 or 3.10)
python3 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt

# Run local server (with python 3.9 or 3.10)
./manage.py makemigrations
./manage.py migrate
./manage.py runserver

# Exit fron venv:
deactivate
```

## Install and run with poetry (Ubuntu)
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.10 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project
git clone https://github.com/Freddsle/ANONCOM
cd ANONCOM/

# Install requirements
poetry env use python3
poetry install 

# Run local server (with python 3.9 or 3.10)
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
