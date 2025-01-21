
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalNomenclatureModule import ChemicalNomenclature







class CASRN(ChemicalNomenclature):
    """
    Class representing the `CASRN` entity, which inherits from:
    - ChemicalNomenclature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d2a47cd8_662f_438f_855a_b4378eb992ff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CASRN'`
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
    obj = CASRN(
    
    class_iri='https://w3id.org/emmo#EMMO_d2a47cd8_662f_438f_855a_b4378eb992ff',
    
    class_name='CASRN',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d2a47cd8_662f_438f_855a_b4378eb992ff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CASRN',
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
    

    
    

    

    