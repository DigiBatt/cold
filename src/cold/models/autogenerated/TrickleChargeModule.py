
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargingModule import Charging







class TrickleCharge(Charging):
    """
    Class representing the `TrickleCharge` entity, which inherits from:
    - Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_fadf9d93_d1fd_492c_a58f_1382e5a5bd47'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TrickleCharge'`
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
    obj = TrickleCharge(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_fadf9d93_d1fd_492c_a58f_1382e5a5bd47',
    
    class_name='TrickleCharge',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_fadf9d93_d1fd_492c_a58f_1382e5a5bd47',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TrickleCharge',
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
    

    
    

    

    