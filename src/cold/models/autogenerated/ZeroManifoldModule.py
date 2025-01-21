
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GeometricalModule import Geometrical







class ZeroManifold(Geometrical):
    """
    Class representing the `ZeroManifold` entity, which inherits from:
    - Geometrical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0ab0485c_9e5b_4257_a679_90a2dfba5c7c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZeroManifold'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZeroManifold(
    
    class_iri='https://w3id.org/emmo#EMMO_0ab0485c_9e5b_4257_a679_90a2dfba5c7c',
    
    class_name='ZeroManifold',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0ab0485c_9e5b_4257_a679_90a2dfba5c7c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZeroManifold',
        alias="class_name"
    )
    

    
    

    

    