import setuptools
from setuptools import find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AIPOC",
    version="0.0.1",
    author="Deepanshu",
    author_email="deepanshubhai84@gmail.com",
    description="AIPOC is an ai assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aipoc-ai/aipoc",
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
