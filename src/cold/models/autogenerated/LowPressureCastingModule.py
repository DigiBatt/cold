
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CastingModule import Casting







class LowPressureCasting(Casting):
    """
    Class representing the `LowPressureCasting` entity, which inherits from:
    - Casting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8b2fd84c_8f51_4731_9bd7_830545e78b23'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LowPressureCasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LowPressureCasting(
    
    class_iri='https://w3id.org/emmo#EMMO_8b2fd84c_8f51_4731_9bd7_830545e78b23',
    
    class_name='LowPressureCasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8b2fd84c_8f51_4731_9bd7_830545e78b23',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LowPressureCasting',
        alias="class_name"
    )
    

    
    

    

    