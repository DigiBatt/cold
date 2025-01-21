
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondaryBatteryModule import SecondaryBattery







class MaintanenceFreeBattery(SecondaryBattery):
    """
    Class representing the `MaintanenceFreeBattery` entity, which inherits from:
    - SecondaryBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_d8b9f2b9_5eb8_4be8_bafa_87789de73434'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaintanenceFreeBattery'`
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
    obj = MaintanenceFreeBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_d8b9f2b9_5eb8_4be8_bafa_87789de73434',
    
    class_name='MaintanenceFreeBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_d8b9f2b9_5eb8_4be8_bafa_87789de73434',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaintanenceFreeBattery',
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
    

    
    

    

    