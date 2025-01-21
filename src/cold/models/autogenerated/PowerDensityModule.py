
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity







class PowerDensity(ElectrochemicalPerformanceQuantity):
    """
    Class representing the `PowerDensity` entity, which inherits from:
    - ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a7eb870c_4ef7_4ccd_85e8_4b7b726d7a2a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PowerDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PowerDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a7eb870c_4ef7_4ccd_85e8_4b7b726d7a2a',
    
    class_name='PowerDensity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a7eb870c_4ef7_4ccd_85e8_4b7b726d7a2a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PowerDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    