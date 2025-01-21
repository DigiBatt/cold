
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumBisoxalatophosphate(CalciumSaltCompound):
    """
    Class representing the `CalciumBisoxalatophosphate` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_1e5c69b2_6dac_44b6_a24e_6170b516cf2c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumBisoxalatophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumBisoxalatophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_1e5c69b2_6dac_44b6_a24e_6170b516cf2c',
    
    class_name='CalciumBisoxalatophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_1e5c69b2_6dac_44b6_a24e_6170b516cf2c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumBisoxalatophosphate',
        alias="class_name"
    )
    

    
    

    

    