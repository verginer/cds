"""Install setup."""
import setuptools

setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version="0.0.1",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",

    description="{{ cookiecutter.description }}",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ]
)
