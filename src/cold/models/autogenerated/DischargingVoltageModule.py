
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellVoltageModule import CellVoltage







class DischargingVoltage(CellVoltage):
    """
    Class representing the `DischargingVoltage` entity, which inherits from:
    - CellVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c7b26177_21bf_4787_b656_8e78edf27f88'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DischargingVoltage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DischargingVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c7b26177_21bf_4787_b656_8e78edf27f88',
    
    class_name='DischargingVoltage',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c7b26177_21bf_4787_b656_8e78edf27f88',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DischargingVoltage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    