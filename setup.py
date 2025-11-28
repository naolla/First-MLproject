from setuptools import find_packages, setup

dot='-e .'
def get_requirements(file_path: str) -> list:
    """This function will return the list of requirements"""

    requirements=[]
    with open(file_path) as requirement_file:
        requirements=requirement_file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if dot in requirements:
            requirements.remove(dot)

    return requirements



setup(
    name="end_to_end_project",
    version="0.0.0.1",
    author="Naol",
    author_email="naolatechshd@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)