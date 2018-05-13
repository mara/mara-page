from setuptools import setup, find_packages

setup(
    name='mara-page',
    version='1.3.0',

    description='Minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure',

    install_requires=[
        'flask>=0.12',
        'pygments>=2.2.0',
        'mara-config>=0.1'
    ],

    dependency_links=[
        'git+https://github.com/mara/mara-config.git@0.1#egg=mara-config-0.1',
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
)
