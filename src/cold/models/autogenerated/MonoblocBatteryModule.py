
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryModule import Battery







class MonoblocBattery(Battery):
    """
    Class representing the `MonoblocBattery` entity, which inherits from:
    - Battery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_84b41796_e958_4740_925c_94c180b91e0f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MonoblocBattery'`
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
    obj = MonoblocBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_84b41796_e958_4740_925c_94c180b91e0f',
    
    class_name='MonoblocBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_84b41796_e958_4740_925c_94c180b91e0f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MonoblocBattery',
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
    

    
    

    

    