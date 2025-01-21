
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ElectrochemicalPerformanceQuantity(ElectrochemicalQuantity):
    """
    Class representing the `ElectrochemicalPerformanceQuantity` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_02eb0465_4f94_453c_8c1f_5ddf80134634'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalPerformanceQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalPerformanceQuantity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_02eb0465_4f94_453c_8c1f_5ddf80134634',
    
    class_name='ElectrochemicalPerformanceQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_02eb0465_4f94_453c_8c1f_5ddf80134634',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalPerformanceQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    