
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FractionUnitModule import FractionUnit







class AreaFractionUnit(FractionUnit):
    """
    Class representing the `AreaFractionUnit` entity, which inherits from:
    - FractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6f4d704a_a7c6_4c07_b8a7_ea0bab04128f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AreaFractionUnit'`
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
    obj = AreaFractionUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_6f4d704a_a7c6_4c07_b8a7_ea0bab04128f',
    
    class_name='AreaFractionUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6f4d704a_a7c6_4c07_b8a7_ea0bab04128f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AreaFractionUnit',
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
    

    
    

    

    