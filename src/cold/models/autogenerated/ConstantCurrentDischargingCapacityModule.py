
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DischargingCapacityModule import DischargingCapacity







class ConstantCurrentDischargingCapacity(DischargingCapacity):
    """
    Class representing the `ConstantCurrentDischargingCapacity` entity, which inherits from:
    - DischargingCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_08833ed2_6324_411a_b34b_fe64c44cd5ef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantCurrentDischargingCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantCurrentDischargingCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_08833ed2_6324_411a_b34b_fe64c44cd5ef',
    
    class_name='ConstantCurrentDischargingCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_08833ed2_6324_411a_b34b_fe64c44cd5ef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantCurrentDischargingCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    