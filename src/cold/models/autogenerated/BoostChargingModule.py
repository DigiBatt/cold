
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargingModule import Charging







class BoostCharging(Charging):
    """
    Class representing the `BoostCharging` entity, which inherits from:
    - Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_02aefb7a_d6ce_4b6e_b854_f7b3d641f670'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BoostCharging'`
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
    obj = BoostCharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_02aefb7a_d6ce_4b6e_b854_f7b3d641f670',
    
    class_name='BoostCharging',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_02aefb7a_d6ce_4b6e_b854_f7b3d641f670',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BoostCharging',
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
    

    
    

    

    