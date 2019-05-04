#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['python-openam', 'requests', 'demjson']


setuptools.setup(
    name='liantis_ess_api',
    version='0.1.1',
    author='dotEsuS',
    author_email='',
    description='Unofficial API wrapper for Liantis ESS',
    long_description=readme,
    url='https://github.com/dotEsuS/liantis_ess_api',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    license="GNU General Public License v3",
)

