
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class CharacterisationHardware(Device):
    """
    Class representing the `CharacterisationHardware` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardware'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationHardware'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationHardware(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardware',
    
    class_name='CharacterisationHardware',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardware',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationHardware',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    