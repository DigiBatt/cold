
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationHardwareModule import CharacterisationHardware







class SamplePreparationInstrument(CharacterisationHardware):
    """
    Class representing the `SamplePreparationInstrument` entity, which inherits from:
    - CharacterisationHardware

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SamplePreparationInstrument'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SamplePreparationInstrument'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SamplePreparationInstrument(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#SamplePreparationInstrument',
    
    class_name='SamplePreparationInstrument',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SamplePreparationInstrument',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SamplePreparationInstrument',
        alias="class_name"
    )
    

    
    

    

    