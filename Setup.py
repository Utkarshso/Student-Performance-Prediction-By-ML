from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    
    requirements = []  ## All information from requirements.txt is come under it 

    with open(file_path) as file_obj:
        requirements = file_obj.readlines() ## reads all the lines from the file
        requirements = [req.replace('\n'," ") for req in requirements]
    
    return requirements


setup(
name='Machine Learning Project',
version='0.0.5',
author = 'Utkarsh',
author_email='utkarshsoni893@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)