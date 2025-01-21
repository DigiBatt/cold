
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell







class StandardVoltageCell(BatteryCell):
    """
    Class representing the `StandardVoltageCell` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_3fcdc2ab_f458_4940_b218_6a10d1764567'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardVoltageCell'`
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
    obj = StandardVoltageCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_3fcdc2ab_f458_4940_b218_6a10d1764567',
    
    class_name='StandardVoltageCell',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_3fcdc2ab_f458_4940_b218_6a10d1764567',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardVoltageCell',
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
    

    
    

    

    