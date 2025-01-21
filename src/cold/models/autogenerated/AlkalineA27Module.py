
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class AlkalineA27(AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `AlkalineA27` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_5ea1c25b_3b25_401c_b6be_76e9f7a4c4bd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineA27'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalineA27(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_5ea1c25b_3b25_401c_b6be_76e9f7a4c4bd',
    
    class_name='AlkalineA27',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_5ea1c25b_3b25_401c_b6be_76e9f7a4c4bd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineA27',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    