
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationHardwareModule import CharacterisationHardware







class SampleInspectionInstrument(CharacterisationHardware):
    """
    Class representing the `SampleInspectionInstrument` entity, which inherits from:
    - CharacterisationHardware

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleInspectionInstrument'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SampleInspectionInstrument'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SampleInspectionInstrument(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleInspectionInstrument',
    
    class_name='SampleInspectionInstrument',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleInspectionInstrument',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SampleInspectionInstrument',
        alias="class_name"
    )
    

    
    

    

    