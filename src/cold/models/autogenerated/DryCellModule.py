
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrimaryBatteryModule import PrimaryBattery







class DryCell(PrimaryBattery):
    """
    Class representing the `DryCell` entity, which inherits from:
    - PrimaryBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_92bc9b20_5de1_40f8_9b55_aff6c3f5e7b0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DryCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DryCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_92bc9b20_5de1_40f8_9b55_aff6c3f5e7b0',
    
    class_name='DryCell',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_92bc9b20_5de1_40f8_9b55_aff6c3f5e7b0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DryCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    