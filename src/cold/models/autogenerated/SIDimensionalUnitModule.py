
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DimensionalUnitModule import DimensionalUnit







class SIDimensionalUnit(DimensionalUnit):
    """
    Class representing the `SIDimensionalUnit` entity, which inherits from:
    - DimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9895a1b4_f0a5_4167_ac5e_97db40b8bfcc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIDimensionalUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIDimensionalUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_9895a1b4_f0a5_4167_ac5e_97db40b8bfcc',
    
    class_name='SIDimensionalUnit',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9895a1b4_f0a5_4167_ac5e_97db40b8bfcc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIDimensionalUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    