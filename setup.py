#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError, err:
    from distutils.core import setup, find_packages

from ace import VERSION

setup(
    name='Axilent-Ace',
    version='.'.join(map(str,VERSION)),
    description='CLI client for Axilent ACE.',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    author='Loren Davie',
    author_email='code@axilent.com',
    url='https://github.com/Axilent/ace-client',
    install_requires=['sharrock-client'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Text Processing',
    ],
    scripts=['scripts/ace'],
)