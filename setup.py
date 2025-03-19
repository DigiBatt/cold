from setuptools import setup, find_packages

setup(
    name="cold",
    version="0.1.0",
    package_dir={"": "cold"},
    packages=find_packages(where="cold"),
    install_requires=[
        "pydantic",  # Add your dependencies here
        "jinja2",
    ],
    extras_require={
        "dev": [
            "rdflib",
            "pydantic",
            "pydantic-schemaorg",
            "requests",
            "jinja2",
            "owlrl",
            "EMMOntoPy"
            ],  # Development dependencies
    },
    entry_points={
        "console_scripts": [
            "generate_models=cold.scripts.regenerate_models:main",
        ],
    },
    python_requires=">=3.7",
    description="A Python package for working with battery ontologies.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DigiBatt/cold",
    author="Simon Clark",
    author_email="your-email@example.com",
)
