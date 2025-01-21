
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GeometricalModule import Geometrical







class ThreeManifold(Geometrical):
    """
    Class representing the `ThreeManifold` entity, which inherits from:
    - Geometrical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_46f0f8df_4dc6_418f_8036_10427a3a288e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThreeManifold'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThreeManifold(
    
    class_iri='https://w3id.org/emmo#EMMO_46f0f8df_4dc6_418f_8036_10427a3a288e',
    
    class_name='ThreeManifold',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_46f0f8df_4dc6_418f_8036_10427a3a288e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThreeManifold',
        alias="class_name"
    )
    

    
    

    

    