
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class PulseCurrent(ElectricCurrent, ElectrochemicalControlQuantity):
    """
    Class representing the `PulseCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_346519a4_006c_496d_8f36_74e38814ed2d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulseCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PulseCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_346519a4_006c_496d_8f36_74e38814ed2d',
    
    class_name='PulseCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_346519a4_006c_496d_8f36_74e38814ed2d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulseCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    