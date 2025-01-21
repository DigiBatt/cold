
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecificEnergyModule import SpecificEnergy







class ChargingSpecificEnergy(SpecificEnergy):
    """
    Class representing the `ChargingSpecificEnergy` entity, which inherits from:
    - SpecificEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5e4490b8_c1dd_4e00_980b_c484e1bf4904'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingSpecificEnergy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingSpecificEnergy(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5e4490b8_c1dd_4e00_980b_c484e1bf4904',
    
    class_name='ChargingSpecificEnergy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5e4490b8_c1dd_4e00_980b_c484e1bf4904',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingSpecificEnergy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    