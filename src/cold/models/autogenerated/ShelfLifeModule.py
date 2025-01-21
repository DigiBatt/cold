
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class ShelfLife(ElectrochemicalPerformanceQuantity):
    """
    Class representing the `ShelfLife` entity, which inherits from:
    - ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e8ec76bf_2a60_4982_8cde_02dfbd2e626f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ShelfLife'`
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
    obj = ShelfLife(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e8ec76bf_2a60_4982_8cde_02dfbd2e626f',
    
    class_name='ShelfLife',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e8ec76bf_2a60_4982_8cde_02dfbd2e626f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ShelfLife',
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
    

    
    

    

    