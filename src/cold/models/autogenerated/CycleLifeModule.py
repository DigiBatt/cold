
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class CycleLife(PureNumberQuantity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `CycleLife` entity, which inherits from:
    - PureNumberQuantity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae782b14_88ce_4cdd_9418_12aca00be937'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CycleLife'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CycleLife(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae782b14_88ce_4cdd_9418_12aca00be937',
    
    class_name='CycleLife',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae782b14_88ce_4cdd_9418_12aca00be937',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CycleLife',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    