
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargingModule import Charging







class FirstCharge(Charging):
    """
    Class representing the `FirstCharge` entity, which inherits from:
    - Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_c6b0d98f_e566_46b1_9dea_635a3299c512'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FirstCharge'`
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
    obj = FirstCharge(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_c6b0d98f_e566_46b1_9dea_635a3299c512',
    
    class_name='FirstCharge',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_c6b0d98f_e566_46b1_9dea_635a3299c512',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FirstCharge',
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
    

    
    

    

    