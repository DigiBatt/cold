
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell







class SwagelokCell(BatteryCell):
    """
    Class representing the `SwagelokCell` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_74d6a5a9_efd6_43de_ad4b_e7b5f6b64aae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SwagelokCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SwagelokCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_74d6a5a9_efd6_43de_ad4b_e7b5f6b64aae',
    
    class_name='SwagelokCell',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_74d6a5a9_efd6_43de_ad4b_e7b5f6b64aae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SwagelokCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    