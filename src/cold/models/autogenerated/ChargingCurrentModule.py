
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellCurrentModule import CellCurrent



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ChargingCurrent(CellCurrent, ElectrochemicalQuantity):
    """
    Class representing the `ChargingCurrent` entity, which inherits from:
    - CellCurrent, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79551e01_4bc6_4292_916e_08fe28a84600'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79551e01_4bc6_4292_916e_08fe28a84600',
    
    class_name='ChargingCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79551e01_4bc6_4292_916e_08fe28a84600',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    