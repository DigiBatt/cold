
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery



from .CoinCellModule import CoinCell





from .CaseModule import Case





class AlkalineA23(AlkalineZincManganeseDioxideBattery, CoinCell):
    """
    Class representing the `AlkalineA23` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery, CoinCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_3ec55c79_6421_4ca3_88c8_a6c98ec6fd0b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineA23'`
        - **Alias**: `class_name`
    
    - `hasCase` (`Optional[Case]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCase`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalineA23(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_3ec55c79_6421_4ca3_88c8_a6c98ec6fd0b',
    
    class_name='AlkalineA23',
    
    hasCase="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_3ec55c79_6421_4ca3_88c8_a6c98ec6fd0b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineA23',
        alias="class_name"
    )
    
    hasCase: Optional[Case] = Field(
        None,
        alias="hasCase"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasCase", pre=True, always=True)
    def validate_hasCase(cls, value):
        if value is not None and not isinstance(value, Case):
            raise ValueError(f"Field 'hasCase' must be an instance of 'Case' or its subclass.")
        return value
    
    

    

    