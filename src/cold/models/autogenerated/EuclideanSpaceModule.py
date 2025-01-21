
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThreeManifoldModule import ThreeManifold







class EuclideanSpace(ThreeManifold):
    """
    Class representing the `EuclideanSpace` entity, which inherits from:
    - ThreeManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5f278af9_8593_4e27_a717_ccc9e07a0ddf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EuclideanSpace'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EuclideanSpace(
    
    class_iri='https://w3id.org/emmo#EMMO_5f278af9_8593_4e27_a717_ccc9e07a0ddf',
    
    class_name='EuclideanSpace',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5f278af9_8593_4e27_a717_ccc9e07a0ddf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EuclideanSpace',
        alias="class_name"
    )
    

    
    

    

    