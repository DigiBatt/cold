
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EnergyDensityModule import EnergyDensity







class DischargingEnergyDensity(EnergyDensity):
    """
    Class representing the `DischargingEnergyDensity` entity, which inherits from:
    - EnergyDensity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4f14e153_cffb_42bd_9a7f_ae40d51ad2cd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DischargingEnergyDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DischargingEnergyDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4f14e153_cffb_42bd_9a7f_ae40d51ad2cd',
    
    class_name='DischargingEnergyDensity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4f14e153_cffb_42bd_9a7f_ae40d51ad2cd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DischargingEnergyDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    