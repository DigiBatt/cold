
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectModule import Object







class SystemResource(Object):
    """
    Class representing the `SystemResource` entity, which inherits from:
    - Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_51f1ba0d_e92b_4be2_9a9d_4640b16ac7ed'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SystemResource'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SystemResource(
    
    class_iri='https://w3id.org/emmo#EMMO_51f1ba0d_e92b_4be2_9a9d_4640b16ac7ed',
    
    class_name='SystemResource',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_51f1ba0d_e92b_4be2_9a9d_4640b16ac7ed',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SystemResource',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    