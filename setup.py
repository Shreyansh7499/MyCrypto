#!/usr/bin/env python3

from setuptools import *

setup(
    name = 'mycrypto',
    author='Shreyansh Nagpal',
    version = '0.1.2',
    description='A CTF helper for Cryptography',
    install_requires = ['gmpy', 'pycryptodome', 'asn1crypto'],
    packages = ['mycrypto']
)