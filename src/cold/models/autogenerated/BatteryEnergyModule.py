
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EnergyModule import Energy



from .BatteryQuantityModule import BatteryQuantity







class BatteryEnergy(Energy, BatteryQuantity):
    """
    Class representing the `BatteryEnergy` entity, which inherits from:
    - Energy, BatteryQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_87bb15ff_4fc2_4929_9938_0b31d9166001'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryEnergy'`
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
    obj = BatteryEnergy(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_87bb15ff_4fc2_4929_9938_0b31d9166001',
    
    class_name='BatteryEnergy',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_87bb15ff_4fc2_4929_9938_0b31d9166001',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryEnergy',
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
    

    
    

    

    