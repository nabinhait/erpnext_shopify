# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0.3'

with open("requirements.txt", "r") as f:
	install_requires = f.readlines()

setup(
    name='erpnext_shopify',
    version=version,
    description='Shopify connector for ERPNext',
    author='Frappe Technologies Pvt. Ltd.',
    author_email='info@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
