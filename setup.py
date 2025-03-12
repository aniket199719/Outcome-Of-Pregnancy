from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'  #automatically triggers setup.py file

#this function returns a list of requirements
def get_requirements(file_path: str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
        name='Outcome of Pregnancy',
        version='0.0.1',
        author='Aniket Walse',
        author_email='aniket.walse20@gmail.com',
        packages=find_packages(),
        install_requires=[get_requirements('requirements.txt')]
    )