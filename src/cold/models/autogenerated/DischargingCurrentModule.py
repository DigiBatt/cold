
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellCurrentModule import CellCurrent



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class DischargingCurrent(CellCurrent, ElectrochemicalQuantity):
    """
    Class representing the `DischargingCurrent` entity, which inherits from:
    - CellCurrent, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e4d666ee_d637_45cd_a904_dc33941ead4f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DischargingCurrent'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DischargingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e4d666ee_d637_45cd_a904_dc33941ead4f',
    
    class_name='DischargingCurrent',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e4d666ee_d637_45cd_a904_dc33941ead4f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DischargingCurrent',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    