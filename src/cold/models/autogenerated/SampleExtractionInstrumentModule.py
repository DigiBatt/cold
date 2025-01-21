
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationHardwareModule import CharacterisationHardware







class SampleExtractionInstrument(CharacterisationHardware):
    """
    Class representing the `SampleExtractionInstrument` entity, which inherits from:
    - CharacterisationHardware

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleExtractionInstrument'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SampleExtractionInstrument'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SampleExtractionInstrument(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleExtractionInstrument',
    
    class_name='SampleExtractionInstrument',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleExtractionInstrument',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SampleExtractionInstrument',
        alias="class_name"
    )
    

    
    

    

    