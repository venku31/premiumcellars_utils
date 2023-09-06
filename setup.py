from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in premiumcellars_utils/__init__.py
from premiumcellars_utils import __version__ as version

setup(
	name="premiumcellars_utils",
	version=version,
	description="Custom utilities",
	author="Premiumcellars",
	author_email="kbajish@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
