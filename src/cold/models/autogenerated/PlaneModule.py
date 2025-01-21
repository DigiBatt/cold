
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TwoManifoldModule import TwoManifold







class Plane(TwoManifold):
    """
    Class representing the `Plane` entity, which inherits from:
    - TwoManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_25f5ca8e_8f7f_44d8_a392_bd3fe8894458'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Plane'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Plane(
    
    class_iri='https://w3id.org/emmo#EMMO_25f5ca8e_8f7f_44d8_a392_bd3fe8894458',
    
    class_name='Plane',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_25f5ca8e_8f7f_44d8_a392_bd3fe8894458',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Plane',
        alias="class_name"
    )
    

    
    

    

    