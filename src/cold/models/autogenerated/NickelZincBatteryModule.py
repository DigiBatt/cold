
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincBatteryModule import ZincBattery







class NickelZincBattery(ZincBattery):
    """
    Class representing the `NickelZincBattery` entity, which inherits from:
    - ZincBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_0c3674b5_3f7b_4308_9bed_0ade6eb69a4e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NickelZincBattery'`
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
    obj = NickelZincBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_0c3674b5_3f7b_4308_9bed_0ade6eb69a4e',
    
    class_name='NickelZincBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_0c3674b5_3f7b_4308_9bed_0ade6eb69a4e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NickelZincBattery',
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
    

    
    

    

    