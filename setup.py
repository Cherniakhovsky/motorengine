#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from motorengine import __version__

tests_require = [
    'nose',
    'coverage',
    'rednose',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'mongoengine',
    'docutils',
    'jinja2',
    'sphinx',
]

setup(
    name='motorengine',
    version=__version__,
    description='MotorEngine is a port of the amazing MongoEngine Mapper. Instead of using pymongo, MotorEngine uses Motor.',
    long_description='''
MotorEngine is a port of the amazing MongoEngine Mapper. Instead of using pymongo, MotorEngine uses Motor.
''',
    keywords='database mongodb tornado python',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='http://github.com/heynemann/motorengine/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pymongo==3.6',
        'tornado',
        'motor==1.2.1',
        'six',
        'easydict'
    ],

    #! Notice:
    # uncomment this
    # If you have enabled the use_2to3 flag, then of course the .egg-link will not link directly to your source code when run under Python 3, since that source code would be made for Python 2 and not work under Python 3. Instead the setup.py develop will build Python 3 code under the build directory, and link there. This means that after doing code changes you will have to run setup.py build before these changes are picked up by your Python 3 installation.
    # [detail](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)
    
    #use_2to3=True,
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
