
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementUnitModule import MeasurementUnit







class SystemUnit(MeasurementUnit):
    """
    Class representing the `SystemUnit` entity, which inherits from:
    - MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3eb993a1_61ae_4a20_b168_dda853f51c14'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SystemUnit'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SystemUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3eb993a1_61ae_4a20_b168_dda853f51c14',
    
    class_name='SystemUnit',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3eb993a1_61ae_4a20_b168_dda853f51c14',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SystemUnit',
        alias="class_name"
    )
    

    
    

    

    