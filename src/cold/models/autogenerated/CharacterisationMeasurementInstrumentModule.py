
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .MeasuringInstrumentModule import MeasuringInstrument



from .CharacterisationHardwareModule import CharacterisationHardware





from .RoleModule import Role





class CharacterisationMeasurementInstrument(Whole, MeasuringInstrument, CharacterisationHardware):
    """
    Class representing the `CharacterisationMeasurementInstrument` entity, which inherits from:
    - Whole, MeasuringInstrument, CharacterisationHardware

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementInstrument'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationMeasurementInstrument'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `hasHolisticPart` (`Optional[Role]`): 
        - **Default Value**: `None`
        - **Alias**: `hasHolisticPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationMeasurementInstrument(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementInstrument',
    
    class_name='CharacterisationMeasurementInstrument',
    
    definition="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    VIMTerm="example_value",
    
    hasHolisticPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementInstrument',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationMeasurementInstrument',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    hasHolisticPart: Optional[Role] = Field(
        None,
        alias="hasHolisticPart"
    )
    

    
    @validator("hasHolisticPart", pre=True, always=True)
    def validate_hasHolisticPart(cls, value):
        if value is not None and not isinstance(value, Role):
            raise ValueError(f"Field 'hasHolisticPart' must be an instance of 'Role' or its subclass.")
        return value
    
    

    

    