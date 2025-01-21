
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RedoxFlowBatteryModule import RedoxFlowBattery





from .ComponentModule import Component





class FullFlowBattery(RedoxFlowBattery):
    """
    Class representing the `FullFlowBattery` entity, which inherits from:
    - RedoxFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_8c808507_976a_4225_8099_604dc7abc5ea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FullFlowBattery'`
        - **Alias**: `class_name`
    
    - `hasComponent` (`Optional[Component]`): 
        - **Default Value**: `None`
        - **Alias**: `hasComponent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FullFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_8c808507_976a_4225_8099_604dc7abc5ea',
    
    class_name='FullFlowBattery',
    
    hasComponent="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_8c808507_976a_4225_8099_604dc7abc5ea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FullFlowBattery',
        alias="class_name"
    )
    
    hasComponent: Optional[Component] = Field(
        None,
        alias="hasComponent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasComponent", pre=True, always=True)
    def validate_hasComponent(cls, value):
        if value is not None and not isinstance(value, Component):
            raise ValueError(f"Field 'hasComponent' must be an instance of 'Component' or its subclass.")
        return value
    
    

    

    