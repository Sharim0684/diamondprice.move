## what is used of setup.py--> to make folder into packages

# if we run pip install -r requirements.txt in setup.py then regressorProject file create when in requirement.txt file in that file -e . is present

# if you want to independently install setup.py then execute a command --> python setup.py install
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name='RegressorProject',
    version='0.0.1',
    author='Sharim',
    author_email='shaikhsharim7@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)