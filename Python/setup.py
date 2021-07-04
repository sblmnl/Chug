from setuptools import setup, find_packages
import os

VERSION = "1.0.0"
DESCRIPTION = "Symmetric encryption algorithm"
LONG_DESCRIPTION = "A symmetric encryption algorithm in which the key is calculated from a known plaintext and a known ciphertext."

setup(
    name="chug",
    version=VERSION,
    author="sblmnl",
    author_email="<sblmnl@protonmail.ch>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "symmetric-encryption", "encryption", "algorithm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
