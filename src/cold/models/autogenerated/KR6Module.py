
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NickelCadmiumBatteryModule import NickelCadmiumBattery







class KR6(NickelCadmiumBattery):
    """
    Class representing the `KR6` entity, which inherits from:
    - NickelCadmiumBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_ad7c1d81_9a9f_4174_88ea_3ba3e8f4dbe2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KR6'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KR6(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_ad7c1d81_9a9f_4174_88ea_3ba3e8f4dbe2',
    
    class_name='KR6',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_ad7c1d81_9a9f_4174_88ea_3ba3e8f4dbe2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'KR6',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    