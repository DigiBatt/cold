
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class LR12(AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `LR12` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_dc2325e3_5a8b_4230_8ad7_fa528fff3059'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LR12'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LR12(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_dc2325e3_5a8b_4230_8ad7_fa528fff3059',
    
    class_name='LR12',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_dc2325e3_5a8b_4230_8ad7_fa528fff3059',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LR12',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    