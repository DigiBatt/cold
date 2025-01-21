
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComponentModule import Component







class CharacterisationComponent(Component):
    """
    Class representing the `CharacterisationComponent` entity, which inherits from:
    - Component

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationComponent'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationComponent'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationComponent(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationComponent',
    
    class_name='CharacterisationComponent',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationComponent',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationComponent',
        alias="class_name"
    )
    

    
    

    

    