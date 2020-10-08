#!/usr/bin/env python3

from setuptools import *

setup(
    name = 'mycrypto',
    author='Shreyansh Nagpal',
    version = '0.1.1',
    description='Implementation of various attacks on CTF Cryptography',
    install_requires = ['gmpy', 'pycryptodome'],
    packages = ['attack_rsa']
)