from setuptools import setup, find_packages

setup(
    name='mara-page',
    version='1.3.0',

    python_requires='>=3.6',
    description='Minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure',

    install_requires=[
        'flask>=0.12',
        'pygments>=2.2.0',
    ],

    dependency_links=[],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
)
