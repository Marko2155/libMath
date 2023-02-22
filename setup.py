from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='libmath',
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords="math, maths",
    version='1.0.0',
    packages=['libmath'],
    url='https://github.com/Marko2155/libmath',
    license='MIT',
    author='Marko Camandioti',
    author_email='camandiotimarko@gmail.com',
    description="A Python library for math.",
    project_urls={
        'Documentation': 'https://github.com/Marko2155/libmath#readme',
        'Source': 'https://github.com/Marko2155/libmath',
        'Tracker': 'https://github.com/Marko2155/libmath/issues',
    }
)
