
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StandardVoltageCellModule import StandardVoltageCell







class WestonStandardVoltageCell(StandardVoltageCell):
    """
    Class representing the `WestonStandardVoltageCell` entity, which inherits from:
    - StandardVoltageCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_54d48300_242b_4af8_96b4_d3436450e094'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WestonStandardVoltageCell'`
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
    obj = WestonStandardVoltageCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_54d48300_242b_4af8_96b4_d3436450e094',
    
    class_name='WestonStandardVoltageCell',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_54d48300_242b_4af8_96b4_d3436450e094',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WestonStandardVoltageCell',
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
    

    
    

    

    