
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementResultModule import MeasurementResult



from .InformationModule import Information



from .CharacterisationDataModule import CharacterisationData







class RawData(MeasurementResult, Information, CharacterisationData):
    """
    Class representing the `RawData` entity, which inherits from:
    - MeasurementResult, Information, CharacterisationData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#RawData'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RawData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RawData(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#RawData',
    
    class_name='RawData',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#RawData',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RawData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    