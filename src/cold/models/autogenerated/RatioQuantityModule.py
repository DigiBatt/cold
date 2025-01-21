
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class RatioQuantity(ISQDimensionlessQuantity):
    """
    Class representing the `RatioQuantity` entity, which inherits from:
    - ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_faab3f84_e475_4a46_af9c_7d249f0b9aef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RatioQuantity'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RatioQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_faab3f84_e475_4a46_af9c_7d249f0b9aef',
    
    class_name='RatioQuantity',
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_faab3f84_e475_4a46_af9c_7d249f0b9aef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RatioQuantity',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    