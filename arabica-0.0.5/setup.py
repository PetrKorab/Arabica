# -*- coding: utf-8 -*


import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

    setuptools.setup(
        name="arabica",
        version="0.0.5",
        author="Petr Koráb",
        author_email="xpetrkorab@gmail.com",
        packages=["arabica"],
        description="A Python package for exploratory analysis of text data",
        long_description=description,
        long_description_content_type="text/markdown",
        url="https://github.com/PetrKorab/Arabica",
        python_requires='>=3.7',
        license='MIT',
        install_requires=['pandas',
                          'nltk>3.6.1',
                          'numpy',
                          'regex',
                          'cleantext']
    )
