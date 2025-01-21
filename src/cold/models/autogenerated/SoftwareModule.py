
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DigitalDataModule import DigitalData







class Software(DigitalData):
    """
    Class representing the `Software` entity, which inherits from:
    - DigitalData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8681074a_e225_4e38_b586_e85b0f43ce38'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Software'`
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
    obj = Software(
    
    class_iri='https://w3id.org/emmo#EMMO_8681074a_e225_4e38_b586_e85b0f43ce38',
    
    class_name='Software',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8681074a_e225_4e38_b586_e85b0f43ce38',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Software',
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
    

    
    

    

    