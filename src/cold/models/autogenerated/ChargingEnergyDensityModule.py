
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EnergyDensityModule import EnergyDensity







class ChargingEnergyDensity(EnergyDensity):
    """
    Class representing the `ChargingEnergyDensity` entity, which inherits from:
    - EnergyDensity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_31a74e23_bb07_41d0_bb8f_1d8cca157503'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingEnergyDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingEnergyDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_31a74e23_bb07_41d0_bb8f_1d8cca157503',
    
    class_name='ChargingEnergyDensity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_31a74e23_bb07_41d0_bb8f_1d8cca157503',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingEnergyDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    