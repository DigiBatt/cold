
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OneManifoldModule import OneManifold







class Circle(OneManifold):
    """
    Class representing the `Circle` entity, which inherits from:
    - OneManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b2a234a8_579a_422c_9305_b8f7e72c76cd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Circle'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Circle(
    
    class_iri='https://w3id.org/emmo#EMMO_b2a234a8_579a_422c_9305_b8f7e72c76cd',
    
    class_name='Circle',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b2a234a8_579a_422c_9305_b8f7e72c76cd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Circle',
        alias="class_name"
    )
    

    
    

    

    