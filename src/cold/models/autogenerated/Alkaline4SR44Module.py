
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery



from .CoinCellModule import CoinCell





from .CaseModule import Case





class Alkaline4SR44(AlkalineZincManganeseDioxideBattery, CoinCell):
    """
    Class representing the `Alkaline4SR44` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery, CoinCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_2e47736e_285a_4215_9c7c_296ae6a45f20'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Alkaline4SR44'`
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
    obj = Alkaline4SR44(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_2e47736e_285a_4215_9c7c_296ae6a45f20',
    
    class_name='Alkaline4SR44',
    
    hasCase="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_2e47736e_285a_4215_9c7c_296ae6a45f20',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Alkaline4SR44',
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
    
    

    

    