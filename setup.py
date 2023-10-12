"""
Setup file for Galactus API.
"""

from setuptools import setup

setup(
    name="galactus",
    packages=[
        "app",
        "app.api",
        "app.middleware",
        "app.models",
        "app.routes",
        "app.services",
        "app.utils",
    ],
    install_requires=[
        "flask",
    ],
    author="Pixelz",
)