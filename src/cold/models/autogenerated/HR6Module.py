
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NickelMetalHydrideBatteryModule import NickelMetalHydrideBattery







class HR6(NickelMetalHydrideBattery):
    """
    Class representing the `HR6` entity, which inherits from:
    - NickelMetalHydrideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a71a4bf2_dee6_4aa4_8ad4_9f38c261fb84'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HR6'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HR6(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a71a4bf2_dee6_4aa4_8ad4_9f38c261fb84',
    
    class_name='HR6',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a71a4bf2_dee6_4aa4_8ad4_9f38c261fb84',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HR6',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    