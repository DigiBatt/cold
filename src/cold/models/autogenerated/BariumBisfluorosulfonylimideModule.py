
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumBisfluorosulfonylimide(BariumSaltCompound):
    """
    Class representing the `BariumBisfluorosulfonylimide` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_7cb7c122_995f_43d3_b419_b8a0d0fe8406'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumBisfluorosulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumBisfluorosulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_7cb7c122_995f_43d3_b419_b8a0d0fe8406',
    
    class_name='BariumBisfluorosulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_7cb7c122_995f_43d3_b419_b8a0d0fe8406',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumBisfluorosulfonylimide',
        alias="class_name"
    )
    

    
    

    

    