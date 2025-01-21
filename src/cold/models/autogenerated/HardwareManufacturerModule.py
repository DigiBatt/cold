
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationHardwareSpecificationModule import CharacterisationHardwareSpecification







class HardwareManufacturer(CharacterisationHardwareSpecification):
    """
    Class representing the `HardwareManufacturer` entity, which inherits from:
    - CharacterisationHardwareSpecification

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareManufacturer'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardwareManufacturer'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardwareManufacturer(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareManufacturer',
    
    class_name='HardwareManufacturer',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationHardwareManufacturer',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardwareManufacturer',
        alias="class_name"
    )
    

    
    

    

    