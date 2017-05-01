"""
pyalgs
-----

Package pyalgs implements algorithms in Robert Sedgwick's Coursera course in Python (Part I and Part II)
"""

import re
import ast
import io
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pyalgs/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(
    name='pyalgs',
    version=version,
    url='https://github.com/chen0040/pyalgs',
    license='BSD',
    author='Xianshun Chen',
    author_email='xs0040@gmail.com',
    description='Python implementation of algorithms on string handling, data structure, graph processing, etc',
    long_description=long_description(),
    packages=['pyalgs'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

__author__ = 'Xianshun Chen'
