# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='erp_xero_connect',
    version=version,
    description='Xero connector for ERPNext',
    author='jevonearth',
    author_email='ebjorsell@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
