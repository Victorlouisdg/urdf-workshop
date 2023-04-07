import setuptools
from setuptools import find_packages

setuptools.setup(
    name="urdf_workshop",
    version="0.0.1",
    author="Victor-Louis De Gusseme",
    author_email="victorlouisdg@gmail.com",
    description="TODO",
    install_requires=[
        "numpy",
    ],
    packages=find_packages(),
    include_package_data=True
)
