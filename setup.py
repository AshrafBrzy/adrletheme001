# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in adrletheme001/__init__.py
from adrletheme001 import __version__ as version

setup(
	name='adrletheme001',
	version=version,
	description='Arabic supported frappe and ERPNext theme for v12 v13',
	author='AshrafBrzy',
	author_email='ashraf@adrle.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
