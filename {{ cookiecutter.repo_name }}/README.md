{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── configs            <- Store all config files. NB passwords and sensitive info goes in .env
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks. Naming convention is a date and title
    │                         (`2016-07-28__initial_exploration.ipynb`).
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── Snakefile          <- Snakemake file for reproducing a full pipeline
    ├── src                <- Source code for use in this project.
    │   ├── data           <- Code to preprocess the data
    │   ├── features       <- Code to turn raw data into features for modeling
    │   ├── models         <- Code to train models and then use trained models to make predictions
    │   ├── rules          <- Scripts meant to be plugged in as Snakemake Rules
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    ├── setup.py           <- Allows installing this project's python code for Notebook importation
    ├── tests              <- unit tests for the code parts (pytest)
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cds project template</a>. Extended by Luca Verginer</p>
