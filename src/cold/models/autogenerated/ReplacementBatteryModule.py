
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryModule import Battery







class ReplacementBattery(Battery):
    """
    Class representing the `ReplacementBattery` entity, which inherits from:
    - Battery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_33d5e843_dcef_4b7b_97ec_bd902c9d950f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReplacementBattery'`
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
    obj = ReplacementBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_33d5e843_dcef_4b7b_97ec_bd902c9d950f',
    
    class_name='ReplacementBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_33d5e843_dcef_4b7b_97ec_bd902c9d950f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReplacementBattery',
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
    

    
    

    

    