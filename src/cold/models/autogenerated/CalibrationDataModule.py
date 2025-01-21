
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationDataModule import CharacterisationData







class CalibrationData(CharacterisationData):
    """
    Class representing the `CalibrationData` entity, which inherits from:
    - CharacterisationData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CalibrationData'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalibrationData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalibrationData(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CalibrationData',
    
    class_name='CalibrationData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CalibrationData',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalibrationData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    