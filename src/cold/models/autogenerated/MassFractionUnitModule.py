
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FractionUnitModule import FractionUnit







class MassFractionUnit(FractionUnit):
    """
    Class representing the `MassFractionUnit` entity, which inherits from:
    - FractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassFractionUnit'`
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
    obj = MassFractionUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1',
    
    class_name='MassFractionUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassFractionUnit',
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
    

    
    

    

    