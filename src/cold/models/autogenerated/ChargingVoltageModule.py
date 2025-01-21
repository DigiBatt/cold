
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellVoltageModule import CellVoltage







class ChargingVoltage(CellVoltage):
    """
    Class representing the `ChargingVoltage` entity, which inherits from:
    - CellVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79a9e1be_35b0_4c3c_8087_b5f967ca0e87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingVoltage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79a9e1be_35b0_4c3c_8087_b5f967ca0e87',
    
    class_name='ChargingVoltage',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79a9e1be_35b0_4c3c_8087_b5f967ca0e87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingVoltage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    