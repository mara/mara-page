from setuptools import setup, find_packages
import re

def get_long_description():
    with open('README.md') as f:
        return re.sub('!\[(.*?)\]\(docs/(.*?)\)', r'![\1](https://github.com/mara/mara-page/raw/master/docs/\2)', f.read())

setup(
    name='mara-page',
    version='1.6.0',

    description='Minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure',

    long_description=get_long_description(),
    long_description_content_type='text/markdown',

    url = 'https://github.com/mara/mara-page',

    python_requires='>=3.6',

    install_requires=[
        'flask>=0.12',
        'pygments>=2.2.0',
    ],

    extras_require={
        'test': ['pytest', 'pytest_click'],
    },

    packages=find_packages(),

    setup_requires=['setuptools_scm'],
    include_package_data=True,

    author='Mara contributors',
    license='MIT',

    entry_points={},
)
