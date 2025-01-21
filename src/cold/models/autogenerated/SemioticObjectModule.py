
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticEntityModule import SemioticEntity







class SemioticObject(SemioticEntity):
    """
    Class representing the `SemioticObject` entity, which inherits from:
    - SemioticEntity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6f5af708_f825_4feb_a0d1_a8d813d3022b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SemioticObject'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SemioticObject(
    
    class_iri='https://w3id.org/emmo#EMMO_6f5af708_f825_4feb_a0d1_a8d813d3022b',
    
    class_name='SemioticObject',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6f5af708_f825_4feb_a0d1_a8d813d3022b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SemioticObject',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    