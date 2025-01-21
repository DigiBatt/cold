
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OneManifoldModule import OneManifold







class Curve(OneManifold):
    """
    Class representing the `Curve` entity, which inherits from:
    - OneManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0ef4ff4a_5458_4f2a_b51f_4689d472a3f2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Curve'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Curve(
    
    class_iri='https://w3id.org/emmo#EMMO_0ef4ff4a_5458_4f2a_b51f_4689d472a3f2',
    
    class_name='Curve',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0ef4ff4a_5458_4f2a_b51f_4689d472a3f2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Curve',
        alias="class_name"
    )
    

    
    

    

    