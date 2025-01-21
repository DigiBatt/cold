
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrimaryBatteryModule import PrimaryBattery







class VoltaicPile(PrimaryBattery):
    """
    Class representing the `VoltaicPile` entity, which inherits from:
    - PrimaryBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_27e95677_3fff_476e_aac9_fe6df5d1535d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VoltaicPile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VoltaicPile(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_27e95677_3fff_476e_aac9_fe6df5d1535d',
    
    class_name='VoltaicPile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_27e95677_3fff_476e_aac9_fe6df5d1535d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VoltaicPile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    