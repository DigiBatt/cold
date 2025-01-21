
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryModule import Battery







class OEMBattery(Battery):
    """
    Class representing the `OEMBattery` entity, which inherits from:
    - Battery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_1c8e08a6_8542_432a_9bd3_9474df55d497'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OEMBattery'`
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
    obj = OEMBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_1c8e08a6_8542_432a_9bd3_9474df55d497',
    
    class_name='OEMBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_1c8e08a6_8542_432a_9bd3_9474df55d497',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OEMBattery',
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
    

    
    

    

    