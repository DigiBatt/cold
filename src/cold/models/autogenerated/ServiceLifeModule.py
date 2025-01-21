
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeModule import Time



from .BatteryQuantityModule import BatteryQuantity







class ServiceLife(Time, BatteryQuantity):
    """
    Class representing the `ServiceLife` entity, which inherits from:
    - Time, BatteryQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_be5d1b4f_5579_4702_9dbb_6c15e577e8dc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ServiceLife'`
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
    obj = ServiceLife(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_be5d1b4f_5579_4702_9dbb_6c15e577e8dc',
    
    class_name='ServiceLife',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_be5d1b4f_5579_4702_9dbb_6c15e577e8dc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ServiceLife',
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
    

    
    

    

    