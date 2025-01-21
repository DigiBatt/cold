
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuantityModule import Quantity



from .SubjectiveModule import Subjective







class SubjectiveProperty(Quantity, Subjective):
    """
    Class representing the `SubjectiveProperty` entity, which inherits from:
    - Quantity, Subjective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a9a6ddf8_7e16_420a_9f3d_df7d5cfe3536'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SubjectiveProperty'`
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
    obj = SubjectiveProperty(
    
    class_iri='https://w3id.org/emmo#EMMO_a9a6ddf8_7e16_420a_9f3d_df7d5cfe3536',
    
    class_name='SubjectiveProperty',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a9a6ddf8_7e16_420a_9f3d_df7d5cfe3536',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SubjectiveProperty',
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
    

    
    

    

    