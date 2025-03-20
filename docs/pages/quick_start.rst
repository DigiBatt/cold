Quick Start
===========
Welcome to the Quick Start Guide for COLD. This guide will help you get up and running with COLD. If you’re new to COLD, we recommend you start here to learn the basics and get a feel for the package.

Getting Started with COLD
-------------------------
COLD is equipped with a series of robust tools that can help you build instances of linked data using ontologies from the EMMO universe. COLD builds on pydantic to translate ontology terms into python data models that can be instantiated, edited, and validated. It is initially developed as a tool for the battery domain, but can be generalized to include other domains as well. 

Since `cold` is not yet available on PyPI, you need to clone the repository and install it manually.

1. **Clone the Repository**  

   .. code-block:: sh

      git clone https://github.com/DigiBatt/cold.git
      cd cold

2. **Create and Activate a Virtual Environment (Recommended)**  

   .. code-block:: sh

      python -m venv .venv
      source .venv/bin/activate  # Windows: .venv\Scripts\activate

3. **Install Dependencies**  

   .. code-block:: sh

      pip install --upgrade pip
      pip install -r requirements.txt

4. **Install cold in Editable Mode**  

   .. code-block:: sh

      pip install -e .

   This allows you to use `cold` while making changes to its source code.

5. **Verify Installation**  

   .. code-block:: python

      import cold
      print(cold.__version__)  # Check that it works

You're all set to use `cold` in your projects!

Exploring Examples
------------------
To help you get acquainted with COLD’s capabilities, we provide a collection of examples that demonstrate common use cases and features of the package:  

- **Jupyter Notebooks**: Interactive notebooks that include detailed explanations alongside the live code, visualisations, and results. These are an excellent resource for learning and can be easily modified and executed to suit your needs.  
- **Python Scripts**: For those who prefer working in a text editor, IDE, or for integrating into larger projects, we provide equivalent examples in plain Python script format.  

You can find these resources in the examples folder of the COLD repository. To access the examples, navigate to the following path after cloning or downloading the repository:  

.. code-block:: sh
    
    path/to/cold/examples

Next Steps
------------------
Once you’re comfortable with the basics demonstrated in the examples, you can dive deeper into the functionality of COLD by delving into the API Reference for detailed API documentation.

Support and Contributions
-------------------------
If you encounter any issues or have questions as you start using COLD, don’t hesitate to reach out to our community:

- GitHub Issues: Report bugs or request new features by opening an `GitHub Issues <https://github.com/DigiBatt/cold/issues>`_  
- Contributions: Interested in contributing to PyBOP? Check out our Contributing Guide for :doc:`guidelines <pages/contributing>`.