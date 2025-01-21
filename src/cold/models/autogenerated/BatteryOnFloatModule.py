
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondaryBatteryModule import SecondaryBattery



from .HolisticSystemModule import HolisticSystem







class BatteryOnFloat(SecondaryBattery, HolisticSystem):
    """
    Class representing the `BatteryOnFloat` entity, which inherits from:
    - SecondaryBattery, HolisticSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_22a6f05f_fdc7_4670_830d_c23062c9ba6b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryOnFloat'`
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
    obj = BatteryOnFloat(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_22a6f05f_fdc7_4670_830d_c23062c9ba6b',
    
    class_name='BatteryOnFloat',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_22a6f05f_fdc7_4670_830d_c23062c9ba6b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryOnFloat',
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
    

    
    

    

    