
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecificCapacityModule import SpecificCapacity







class ChargingSpecificCapacity(SpecificCapacity):
    """
    Class representing the `ChargingSpecificCapacity` entity, which inherits from:
    - SpecificCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4882cf2f_aab7_4a3a_a103_7f56b55fbed3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingSpecificCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingSpecificCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4882cf2f_aab7_4a3a_a103_7f56b55fbed3',
    
    class_name='ChargingSpecificCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4882cf2f_aab7_4a3a_a103_7f56b55fbed3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingSpecificCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    