
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TwoManifoldModule import TwoManifold







class Sphere(TwoManifold):
    """
    Class representing the `Sphere` entity, which inherits from:
    - TwoManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d7bf784a_db94_4dd9_861c_54f262846fbf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Sphere'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Sphere(
    
    class_iri='https://w3id.org/emmo#EMMO_d7bf784a_db94_4dd9_861c_54f262846fbf',
    
    class_name='Sphere',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d7bf784a_db94_4dd9_861c_54f262846fbf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Sphere',
        alias="class_name"
    )
    

    
    

    

    