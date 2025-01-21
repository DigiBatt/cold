
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class LR1(AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `LR1` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_1c0306f5_5698_4874_b6ce_e5cc45a46b91'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LR1'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LR1(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_1c0306f5_5698_4874_b6ce_e5cc45a46b91',
    
    class_name='LR1',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_1c0306f5_5698_4874_b6ce_e5cc45a46b91',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LR1',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    