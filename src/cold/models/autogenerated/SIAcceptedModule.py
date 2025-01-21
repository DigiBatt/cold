
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementUnitModule import MeasurementUnit







class SIAccepted(MeasurementUnit):
    """
    Class representing the `SIAccepted` entity, which inherits from:
    - MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e8b5f7de_4fd9_41d7_b988_87b512fe0180'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIAccepted'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIAccepted(
    
    class_iri='https://w3id.org/emmo#EMMO_e8b5f7de_4fd9_41d7_b988_87b512fe0180',
    
    class_name='SIAccepted',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e8b5f7de_4fd9_41d7_b988_87b512fe0180',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIAccepted',
        alias="class_name"
    )
    

    
    

    

    