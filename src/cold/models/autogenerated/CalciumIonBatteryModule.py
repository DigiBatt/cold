
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumBatteryModule import CalciumBattery







class CalciumIonBattery(CalciumBattery):
    """
    Class representing the `CalciumIonBattery` entity, which inherits from:
    - CalciumBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_2099e6d6_680b_476c_a123_f6c89ff93389'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumIonBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumIonBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_2099e6d6_680b_476c_a123_f6c89ff93389',
    
    class_name='CalciumIonBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_2099e6d6_680b_476c_a123_f6c89ff93389',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumIonBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    