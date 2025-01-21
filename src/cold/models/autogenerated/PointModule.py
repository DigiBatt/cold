
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZeroManifoldModule import ZeroManifold







class Point(ZeroManifold):
    """
    Class representing the `Point` entity, which inherits from:
    - ZeroManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_39362460_2a97_4367_8f93_0418c2ac9a08'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Point'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Point(
    
    class_iri='https://w3id.org/emmo#EMMO_39362460_2a97_4367_8f93_0418c2ac9a08',
    
    class_name='Point',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_39362460_2a97_4367_8f93_0418c2ac9a08',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Point',
        alias="class_name"
    )
    

    
    

    

    