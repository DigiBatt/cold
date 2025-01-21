
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CylindricalBatteryModule import CylindricalBattery



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class LR03(CylindricalBattery, AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `LR03` entity, which inherits from:
    - CylindricalBattery, AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a5299801_2a8d_4d03_a476_ca2c5e9ca702'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LR03'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LR03(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a5299801_2a8d_4d03_a476_ca2c5e9ca702',
    
    class_name='LR03',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a5299801_2a8d_4d03_a476_ca2c5e9ca702',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LR03',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    