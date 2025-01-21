
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PropertyModule import Property







class CharacterisationHardwareSpecification(Property):
    """
    Class representing the `CharacterisationHardwareSpecification` entity, which inherits from:
    - Property

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareSpecification'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationHardwareSpecification'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationHardwareSpecification(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareSpecification',
    
    class_name='CharacterisationHardwareSpecification',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareSpecification',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationHardwareSpecification',
        alias="class_name"
    )
    

    
    

    

    