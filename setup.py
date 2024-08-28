import os, sys, re
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop

FILE_PATH = os.path.abspath(__file__)
PROJ_PATH = os.path.dirname(FILE_PATH)
SRC_PATH = os.path.join(PROJ_PATH, 'filesystem')

def read_version() -> str:
    version_path = os.path.join(PROJ_PATH, 'version')
    with open(version_path, 'r') as file:
        version = file.read().strip()
    print(f'version: {version}')
    return version

class InstallCommand(install):
    def run(self):
        os.system('pip install -r requirements.txt')
        super().run()

class DevelopCommand(develop):
    def run(self):
        os.system('pip install -r requirements.txt')
        super().run()

setup(
    name='filesystem',
    version=read_version(),
    description="Wrapper package for filesystem interactions.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Lance Lee',
    author_email='belanced@gmail.com',
    url='https://github.com/belanced/filesystem',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8, <3.11',
    packages=find_packages(include=['filesystem', 'filesystem/*']),
    include_package_data=True,
    zip_safe=False,
    cmdclass={
        'install': InstallCommand,
        'develop': DevelopCommand,
    },
)
