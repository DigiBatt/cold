
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumBisfluorosulfonylimide(CalciumSaltCompound):
    """
    Class representing the `CalciumBisfluorosulfonylimide` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_fe5452de_6d49_4f60_9a15_a022bb5219a2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumBisfluorosulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumBisfluorosulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_fe5452de_6d49_4f60_9a15_a022bb5219a2',
    
    class_name='CalciumBisfluorosulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_fe5452de_6d49_4f60_9a15_a022bb5219a2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumBisfluorosulfonylimide',
        alias="class_name"
    )
    

    
    

    

    