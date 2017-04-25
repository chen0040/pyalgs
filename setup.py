"""
pyalgs
-----

Package pyalgs implements algorithms in Robert Sedgwick's Coursera course in Python (Part I and Part II)

"""
import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pyalgs/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='pyalgs',
    version=version,
    url='https://github.com/chen0040/pyalgs',
    license='BSD',
    author='Xianshun Chen',
    author_email='xs0040@gmail.com',
    description='Python implementation of Robert Sedgwick\'s Algorithm (Part I and Part II) Coursera course',
    long_description=__doc__,
    packages=['pyalgs'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Algorithms :: Basic :: Data Structure',
        'Topic :: Algorithms :: Basic :: Graph Processing',
        'Topic :: Algorithms :: Basic :: String Processing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)