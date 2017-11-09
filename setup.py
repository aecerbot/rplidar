#!/usr/bin/env python3
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'aerplidar',
    py_modules = ['aerplidar'],
    version = '0.0.1',
    description = 'Simple and lightweight module for working with RPLidar laser scanners',
    author='Artyom Pavlov, Roger Donaldson',
    author_email='roger@aecerbot.ca',
    url='https://github.com/aecerbot/rplidar',
    license='MIT',
    install_requires=['pyserial'],
    zip_safe=True,
    long_description='This module aims to implement communication protocol '
        'with RPLidar laser scanners. It\'s Python 2 and 3 '
        'compatible but was mainly tested using Python 3.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Hardware',
    ],
)
