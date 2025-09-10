# COLD: Constructing Ontology-based Linked Data

<img src="docs/assets/img/cold_logo.png" alt="cold-logo" width="100%">

COLD is a Python package for generating and validating battery-related linked data. It provides tools for structuring battery metadata and test data into RDF/JSON-LD formats using an ontology-driven approach. cold ensures that generated data adheres to well-defined ontologies, making it easy to integrate with semantic web technologies and battery digital twin ecosystems.

## Features

- Ontology-Driven Linked Data Generation: Creates structured RDF/JSON-LD descriptions using EMMO and domain-specific battery ontologies.  
- Validation of Linked Data: Ensures data correctness by checking against predefined ontology schemas.  
- Metadata Structuring: Transforms raw battery test data into standardized linked data formats.  
- Seamless Integration: Designed to work with battery ontologies and digital twin ecosystems.  

## Usage

## Roadmap

- Enhanced Ontology Support: Expanding compatibility with more battery domain ontologies.  
- Improved Validation Features: More detailed error reporting and schema checking.  
- Extended Metadata Handling: Support for additional battery test data types.  

## Installation
- Navigate to repository  install using 
`pip install -e . `

## Autogenerating python classes
- Before running for the first time, and every time the ontology changes you need to regenerate the python classes for each item.
`python ./cold/scripts/regenerate_models.py`

## Examples

- The examples directory contains scripts for common example models. 
- e.g. creating a json-LD model for a CR2032 cell. [./cold/examples/scripts/example_cr2032.py](./cold/examples/scripts/example_cr2032.py)

## Contributing

Contributions are welcome! To contribute:  

1. Fork the repository  
2. Create a new branch (feature-branch)  
3. Commit your changes  
4. Push to your branch and create a pull request  

## License