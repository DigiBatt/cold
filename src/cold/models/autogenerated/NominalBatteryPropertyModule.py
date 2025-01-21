
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NominalPropertyModule import NominalProperty







class NominalBatteryProperty(NominalProperty):
    """
    Class representing the `NominalBatteryProperty` entity, which inherits from:
    - NominalProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_fb9baf9b_680e_493e_a755_da9bb1fc9fae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NominalBatteryProperty'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NominalBatteryProperty(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_fb9baf9b_680e_493e_a755_da9bb1fc9fae',
    
    class_name='NominalBatteryProperty',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_fb9baf9b_680e_493e_a755_da9bb1fc9fae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NominalBatteryProperty',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    