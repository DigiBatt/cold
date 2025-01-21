
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class StepSignalCurrent(ElectricCurrent, ElectrochemicalControlQuantity):
    """
    Class representing the `StepSignalCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6769536b_5320_4b48_a2d8_ac285ec635a8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StepSignalCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StepSignalCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6769536b_5320_4b48_a2d8_ac285ec635a8',
    
    class_name='StepSignalCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6769536b_5320_4b48_a2d8_ac285ec635a8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StepSignalCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    