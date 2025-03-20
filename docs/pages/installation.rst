Installation
============
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