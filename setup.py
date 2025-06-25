
from setuptools import setup, find_packages

setup(
    name="viarag-sdk",
    version="0.2.0",
    description="Python SDK for ViaRAG, a seamless RAG integration pipeline",
    author="ViaVeritas",
    author_email="team@viaveri.co",
    url="https://github.com/ViaVeritas/ViaRAG_SDK",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pydantic>=1.10.0",
        "toml>=0.10.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires=">=3.7",
)
