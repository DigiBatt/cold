
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FractionUnitModule import FractionUnit







class AmountFractionUnit(FractionUnit):
    """
    Class representing the `AmountFractionUnit` entity, which inherits from:
    - FractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f76f5a24_d703_4e8c_b368_f9a7777cb73a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmountFractionUnit'`
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
    obj = AmountFractionUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_f76f5a24_d703_4e8c_b368_f9a7777cb73a',
    
    class_name='AmountFractionUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f76f5a24_d703_4e8c_b368_f9a7777cb73a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmountFractionUnit',
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
    

    
    

    

    