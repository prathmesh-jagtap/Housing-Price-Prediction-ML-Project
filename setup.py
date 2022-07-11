from setuptools import find_packages, setup
from typing import List


# Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Ineuron Project"
DESCRIPTION = "This is a first NOV FSDS machine learning project"
# PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    '''
    Description : This functio read the liberaries form requirements 
    and gives the results in form of list of string

    Return :- returns the list of all liberaries
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace(
            "\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    license="Apache License",
    install_requires=get_requirements_list()
)
