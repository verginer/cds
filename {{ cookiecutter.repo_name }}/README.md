{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
--------------------

.. code-block:: none

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make article`
    ├── README.md          <- The top-level README for authors using this project.
    ├── configs            <- Store all config files. NB passwords and sensitive info go in .env
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── notebooks          <- Jupyter notebooks. Naming convention is a date and title
    │                         (`2016-07-28_initial_exploration.ipynb`).
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── article            <- Directory containing the root `article.tex` to be written
    │   └── figures        <- Generated graphics and figures to be used in article.
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
                                generated with `conda env export > environment.yml`
    ├── Snakefile          <- Snakemake file for reproducing the full pipeline (raw -> processed)
    ├── src                <- Source code for use in this project.
    │   ├── data           <- Code to preprocess the data
    │   ├── features       <- Code to turn raw data into features for modeling
    │   ├── models         <- Code for the modelling of the empirical data or simulations
    │   ├── rules          <- Scripts to be plugged in as Snakemake Rules
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    ├── setup.py           <- Allows installing this project's python code for Notebook importation
    ├── setup.cfg          <- Place for configuration of various python dev tools (i.e. pytest, flake8, ...)
    └── tests              <- unit tests for the code parts (pytest)


--------

forked from https://drivendata.github.io/cookiecutter-data-science/.
