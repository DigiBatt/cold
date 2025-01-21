
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConstituentModule import Constituent



from .BatteryModule import Battery





from .ConstituentModule import Constituent





class BatteryModule(Constituent, Battery):
    """
    Class representing the `BatteryModule` entity, which inherits from:
    - Constituent, Battery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_9acfeea6_ca7f_4b97_9844_c38edf6387ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryModule'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BatteryModule(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_9acfeea6_ca7f_4b97_9844_c38edf6387ec',
    
    class_name='BatteryModule',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_9acfeea6_ca7f_4b97_9844_c38edf6387ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryModule',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    