
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalFormulaModule import ChemicalFormula







class CondensedFormula(ChemicalFormula):
    """
    Class representing the `CondensedFormula` entity, which inherits from:
    - ChemicalFormula

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bf836c2b_7800_474d_b674_f5d629fa0bb1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CondensedFormula'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CondensedFormula(
    
    class_iri='https://w3id.org/emmo#EMMO_bf836c2b_7800_474d_b674_f5d629fa0bb1',
    
    class_name='CondensedFormula',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bf836c2b_7800_474d_b674_f5d629fa0bb1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CondensedFormula',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    