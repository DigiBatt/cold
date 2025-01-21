
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .BatteryQuantityModule import BatteryQuantity







class DepthOfDischarge(RatioQuantity, BatteryQuantity):
    """
    Class representing the `DepthOfDischarge` entity, which inherits from:
    - RatioQuantity, BatteryQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_22353114_9b0a_42d1_b96c_3a702c273e2d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DepthOfDischarge'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DepthOfDischarge(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_22353114_9b0a_42d1_b96c_3a702c273e2d',
    
    class_name='DepthOfDischarge',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_22353114_9b0a_42d1_b96c_3a702c273e2d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DepthOfDischarge',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    