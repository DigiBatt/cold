
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalFormulaModule import ChemicalFormula







class EmpiricalFormula(ChemicalFormula):
    """
    Class representing the `EmpiricalFormula` entity, which inherits from:
    - ChemicalFormula

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6afdb7e8_2a0b_444d_bde3_8d67d98180c0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EmpiricalFormula'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EmpiricalFormula(
    
    class_iri='https://w3id.org/emmo#EMMO_6afdb7e8_2a0b_444d_bde3_8d67d98180c0',
    
    class_name='EmpiricalFormula',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6afdb7e8_2a0b_444d_bde3_8d67d98180c0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EmpiricalFormula',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    