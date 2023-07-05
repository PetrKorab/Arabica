# -*- coding: utf-8 -*


import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

    setuptools.setup(
        name="arabica",
        version="1.6.8",
        author="Petr Koráb",
        author_email="xpetrkorab@gmail.com",
        packages=["arabica"],
        description="Python package for exploratory text data analysis",
        long_description=description,
        long_description_content_type="text/markdown",
        url="https://github.com/PetrKorab/Arabica",
        python_requires='>3.6, <3.11',
        install_requires = ['pandas >= 1.4.0',
                            'nltk == 3.6.2',
                            'regex == 2022.10.31',
                            'finvader',
                            'matplotlib == 3.6.0',
                            'matplotlib-inline == 0.1.6',
                            'plotnine == 0.10.1',
                            'wordcloud == 1.8.2.2',
                            'jenkspy == 0.3.2',
                            'vaderSentiment == 3.3.2',
                            'cleantext == 1.1.4'],
        license='OSI Approved :: Apache Software License'
    )
