
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargingModule import Charging







class Overcharging(Charging):
    """
    Class representing the `Overcharging` entity, which inherits from:
    - Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9ee6e728_e8f5_4b36_a045_d63da69dfc85'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Overcharging'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Overcharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9ee6e728_e8f5_4b36_a045_d63da69dfc85',
    
    class_name='Overcharging',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9ee6e728_e8f5_4b36_a045_d63da69dfc85',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Overcharging',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    