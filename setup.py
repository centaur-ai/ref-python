from setuptools import setup, find_packages

setup(
    name='centaur',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',  # Example dependency
    ],
    entry_points={
        'console_scripts': [
            'project_name=project_name.main:main',
        ],
    },
)
