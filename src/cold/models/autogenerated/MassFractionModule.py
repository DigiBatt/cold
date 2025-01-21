
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassFractionUnitModule import MassFractionUnit







class MassFraction(MassFractionUnit):
    """
    Class representing the `MassFraction` entity, which inherits from:
    - MassFractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/disciplines/units/coherentsiunits#EMMO_089f13b1_ceb3_4d2a_8795_b4a2d92916da'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassFraction'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassFraction(
    
    class_iri='https://w3id.org/emmo/disciplines/units/coherentsiunits#EMMO_089f13b1_ceb3_4d2a_8795_b4a2d92916da',
    
    class_name='MassFraction',
    
    elucidation="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/disciplines/units/coherentsiunits#EMMO_089f13b1_ceb3_4d2a_8795_b4a2d92916da',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassFraction',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    unitSymbol: Optional[str] = Field(
        None,
        alias="unitSymbol"
    )
    

    
    

    

    