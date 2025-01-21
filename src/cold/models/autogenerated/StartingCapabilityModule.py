
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PowerModule import Power



from .BatteryQuantityModule import BatteryQuantity







class StartingCapability(Power, BatteryQuantity):
    """
    Class representing the `StartingCapability` entity, which inherits from:
    - Power, BatteryQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a882d3a6_e055_4743_8fc6_5510485dcfe2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StartingCapability'`
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
    obj = StartingCapability(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a882d3a6_e055_4743_8fc6_5510485dcfe2',
    
    class_name='StartingCapability',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a882d3a6_e055_4743_8fc6_5510485dcfe2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StartingCapability',
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
    

    
    

    

    