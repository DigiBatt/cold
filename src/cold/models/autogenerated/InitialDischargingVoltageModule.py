
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DischargingVoltageModule import DischargingVoltage







class InitialDischargingVoltage(DischargingVoltage):
    """
    Class representing the `InitialDischargingVoltage` entity, which inherits from:
    - DischargingVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74861991_7da2_4e0f_b6c1_b16713f538bf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InitialDischargingVoltage'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InitialDischargingVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74861991_7da2_4e0f_b6c1_b16713f538bf',
    
    class_name='InitialDischargingVoltage',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74861991_7da2_4e0f_b6c1_b16713f538bf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InitialDischargingVoltage',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    