
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EquationModule import Equation







class MaterialRelation(Equation):
    """
    Class representing the `MaterialRelation` entity, which inherits from:
    - Equation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e5438930_04e7_4d42_ade5_3700d4a52ab7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaterialRelation'`
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
    obj = MaterialRelation(
    
    class_iri='https://w3id.org/emmo#EMMO_e5438930_04e7_4d42_ade5_3700d4a52ab7',
    
    class_name='MaterialRelation',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e5438930_04e7_4d42_ade5_3700d4a52ab7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaterialRelation',
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
    

    
    

    

    