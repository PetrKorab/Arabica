# -*- coding: utf-8 -*


import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

    setuptools.setup(
        name="arabica",
        version="1.0.2",
        author="Petr Koráb",
        author_email="xpetrkorab@gmail.com",
        packages=["arabica"],
        description="Python package for exploratory text data analysis",
        long_description=description,
        long_description_content_type="text/markdown",
        url="https://github.com/PetrKorab/Arabica",
        python_requires='>=3.7',
        license='MIT',
        install_requires=['pandas',
                          'nltk>3.6.1',
                          'numpy>=1.21.6',
                          'regex',
                          'cleantext>=1.1.4']
    )