from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='asgard-api-sdk',
    version='0.3.0',

    description='Asgard API common code',
    long_description="Conjunto de código que são úteis para os plugins da Asgard API",
    url='https://github.com/B2W-BIT/asgard-api-sdk',
    # Author details
    author='Dalton Barreto',
    author_email='',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    entry_points={
    },
)
