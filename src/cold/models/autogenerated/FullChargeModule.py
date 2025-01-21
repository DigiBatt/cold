
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StateOfChargeModule import StateOfCharge







class FullCharge(StateOfCharge):
    """
    Class representing the `FullCharge` entity, which inherits from:
    - StateOfCharge

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_1cfab1de_8a2c_49cd_abbe_a71a3f1ba78c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FullCharge'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FullCharge(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_1cfab1de_8a2c_49cd_abbe_a71a3f1ba78c',
    
    class_name='FullCharge',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_1cfab1de_8a2c_49cd_abbe_a71a3f1ba78c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FullCharge',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    