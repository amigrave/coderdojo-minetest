#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from mcpi import VERSION

with open('README.md') as f:
    long_description = f.read()

setup(
    name="coderdojo-minetest",
    version=VERSION,
    author="Fabien Meghazi",
    author_email="agr@amigrave.com",
    license="MIT",
    description="CoderDojo workshop module for minetest",
    long_description=long_description,
    keywords="CoderDojo minetest",
    url="https://github.com/amigrave/coderdojo-minetest",
    py_modules=["mcpi"],
    packages=find_packages(),
)
