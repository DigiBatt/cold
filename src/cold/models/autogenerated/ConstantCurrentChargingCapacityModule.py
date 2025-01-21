
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargingCapacityModule import ChargingCapacity







class ConstantCurrentChargingCapacity(ChargingCapacity):
    """
    Class representing the `ConstantCurrentChargingCapacity` entity, which inherits from:
    - ChargingCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_37c38b7e_9ded_481a_85fd_a467f1ee2b9f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantCurrentChargingCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantCurrentChargingCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_37c38b7e_9ded_481a_85fd_a467f1ee2b9f',
    
    class_name='ConstantCurrentChargingCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_37c38b7e_9ded_481a_85fd_a467f1ee2b9f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantCurrentChargingCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    