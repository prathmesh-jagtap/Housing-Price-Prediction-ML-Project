from setuptools import find_packages, setup
from typing import List


# Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Ineuron Project"
DESCRIPTION = "This is a first NOV FSDS machine learning project"
# PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description : This functio read the liberaries form requirements 
    and gives the results in form of list of string
    
    Return :- returns the list of all liberaries
    '''
    with open(REQUIREMENTS_FILE_NAME, 'r') as requirements:
        return requirements.readlines().remove("-e .")

setup( 
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages = find_packages(),
    license = "Apache License",
    install_requires = get_requirements_list()
)

