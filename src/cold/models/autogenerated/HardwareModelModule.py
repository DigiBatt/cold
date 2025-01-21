
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationHardwareSpecificationModule import CharacterisationHardwareSpecification







class HardwareModel(CharacterisationHardwareSpecification):
    """
    Class representing the `HardwareModel` entity, which inherits from:
    - CharacterisationHardwareSpecification

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareModel'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardwareModel'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardwareModel(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareModel',
    
    class_name='HardwareModel',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareModel',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardwareModel',
        alias="class_name"
    )
    

    
    

    

    