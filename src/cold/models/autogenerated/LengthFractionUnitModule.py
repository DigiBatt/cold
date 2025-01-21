
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FractionUnitModule import FractionUnit







class LengthFractionUnit(FractionUnit):
    """
    Class representing the `LengthFractionUnit` entity, which inherits from:
    - FractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cdc962d8_f3ea_4764_a57a_c7caa4859179'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LengthFractionUnit'`
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
    obj = LengthFractionUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_cdc962d8_f3ea_4764_a57a_c7caa4859179',
    
    class_name='LengthFractionUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cdc962d8_f3ea_4764_a57a_c7caa4859179',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LengthFractionUnit',
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
    

    
    

    

    