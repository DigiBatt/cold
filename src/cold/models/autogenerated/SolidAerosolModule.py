
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AerosolModule import Aerosol







class SolidAerosol(Aerosol):
    """
    Class representing the `SolidAerosol` entity, which inherits from:
    - Aerosol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_96c8d72f_b436_44e2_9f7f_085c24094292'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidAerosol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidAerosol(
    
    class_iri='https://w3id.org/emmo#EMMO_96c8d72f_b436_44e2_9f7f_085c24094292',
    
    class_name='SolidAerosol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_96c8d72f_b436_44e2_9f7f_085c24094292',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidAerosol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    