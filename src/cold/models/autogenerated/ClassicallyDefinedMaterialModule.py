
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialModule import Material







class ClassicallyDefinedMaterial(Material):
    """
    Class representing the `ClassicallyDefinedMaterial` entity, which inherits from:
    - Material

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_39348191_08fd_4bb6_9b1e_012d5b2f1ff6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ClassicallyDefinedMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ClassicallyDefinedMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_39348191_08fd_4bb6_9b1e_012d5b2f1ff6',
    
    class_name='ClassicallyDefinedMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_39348191_08fd_4bb6_9b1e_012d5b2f1ff6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ClassicallyDefinedMaterial',
        alias="class_name"
    )
    

    
    

    

    