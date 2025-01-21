
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectModule import Object







class ComputerSystem(Object):
    """
    Class representing the `ComputerSystem` entity, which inherits from:
    - Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e7848014_ad79_422d_be02_74df892f7c11'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ComputerSystem'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ComputerSystem(
    
    class_iri='https://w3id.org/emmo#EMMO_e7848014_ad79_422d_be02_74df892f7c11',
    
    class_name='ComputerSystem',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e7848014_ad79_422d_be02_74df892f7c11',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ComputerSystem',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    