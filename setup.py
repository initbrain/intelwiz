#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
from setuptools import setup, find_packages

from intelwiz import NAME, VERSION, AUTHOR, CONTACT

CURRENT_DIR = os.path.dirname(__file__)

README_PATH = os.path.join(CURRENT_DIR, 'README')
if os.path.exists(README_PATH):
    with open(README_PATH) as readme:
        README = readme.read().strip()
else:
    README = ''

REQUIREMENTS_PATH = os.path.join(CURRENT_DIR, 'requirements.txt')
if os.path.exists(REQUIREMENTS_PATH):
    with open(REQUIREMENTS_PATH) as requirements:
        REQUIREMENTS = requirements.read().strip()
else:
    REQUIREMENTS = ''

setup(
    name=NAME,
    version=VERSION,
    description="Intelligence Wizard",
    long_description=README,
    author=AUTHOR,
    author_email=CONTACT,
    url='http://www.initbrain.fr',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'intelwiz_bootstrap = intelwiz.interfaces.install:main',
            'intelwiz = intelwiz.interfaces.gui:main'
            #'intelwiz_cli = intelwiz.interface.cli:main' #TODO
        ]
    },
    data_files=[
        ('intelwiz/images/', ['intelwiz/images/icone.png',
                               'intelwiz/images/a_propos.png']),
        ('intelwiz/core/', ['intelwiz/core/modules.json'])
    ]
)

os.system('intelwiz_bootstrap')
