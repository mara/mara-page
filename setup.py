from setuptools import setup, find_packages

setup(
    name='mara-page',
    version='1.4.1',

    description='Minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure',

    python_requires='>=3.6',

    install_requires=[
        'flask>=0.12',
        'pygments>=2.2.0',
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
)
