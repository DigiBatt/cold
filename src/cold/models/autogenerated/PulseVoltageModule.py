
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellVoltageModule import CellVoltage



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class PulseVoltage(CellVoltage, ElectrochemicalControlQuantity):
    """
    Class representing the `PulseVoltage` entity, which inherits from:
    - CellVoltage, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d2b102b_3515_4591_b079_69232c44f9dc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulseVoltage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PulseVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d2b102b_3515_4591_b079_69232c44f9dc',
    
    class_name='PulseVoltage',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d2b102b_3515_4591_b079_69232c44f9dc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulseVoltage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    