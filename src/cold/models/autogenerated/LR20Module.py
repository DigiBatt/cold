
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class LR20(AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `LR20` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_0c9979c2_c981_48ea_a8e1_72bdcb58fd58'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LR20'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LR20(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_0c9979c2_c981_48ea_a8e1_72bdcb58fd58',
    
    class_name='LR20',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_0c9979c2_c981_48ea_a8e1_72bdcb58fd58',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LR20',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    