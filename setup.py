import os
from setuptools import setup, find_packages


setup(
    name='random-chars-generator',
    version='0.1',
    author='Aaron Lelevier',
    author_email='pyaaron@gmail.com',
    description='Random genrator for differnt types in Python',
    long_description=read('README.md'),
    url='https://github.com/aronysidoro/random-chars-generator',
    license='MIT',
    keywords=['django'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=['randoms'],
    zip_safe=False,
)