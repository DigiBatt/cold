
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GeometricalModule import Geometrical







class OneManifold(Geometrical):
    """
    Class representing the `OneManifold` entity, which inherits from:
    - Geometrical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0c576e13_4ee7_4f3d_bfe9_1614243df018'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OneManifold'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OneManifold(
    
    class_iri='https://w3id.org/emmo#EMMO_0c576e13_4ee7_4f3d_bfe9_1614243df018',
    
    class_name='OneManifold',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0c576e13_4ee7_4f3d_bfe9_1614243df018',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OneManifold',
        alias="class_name"
    )
    

    
    

    

    