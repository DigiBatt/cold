
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class BatteryTray(Device):
    """
    Class representing the `BatteryTray` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_bcf8f9dd_f493_4547_a5a3_e14b1f4c0f5f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryTray'`
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
    obj = BatteryTray(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_bcf8f9dd_f493_4547_a5a3_e14b1f4c0f5f',
    
    class_name='BatteryTray',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_bcf8f9dd_f493_4547_a5a3_e14b1f4c0f5f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryTray',
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
    

    
    

    

    