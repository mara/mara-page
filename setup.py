from setuptools import setup, find_packages

setup(
    name='mara-page',
    version='1.0.0',

    description='Minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure',

    install_requires=[
        "flask>=0.12",
    ],

    dependency_links=[],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
)
