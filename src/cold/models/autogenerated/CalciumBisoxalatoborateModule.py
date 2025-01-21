
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumBisoxalatoborate(CalciumSaltCompound):
    """
    Class representing the `CalciumBisoxalatoborate` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_9d6b0e6b_b51f_40a8_bc9d_1418ea5356b1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumBisoxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumBisoxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_9d6b0e6b_b51f_40a8_bc9d_1418ea5356b1',
    
    class_name='CalciumBisoxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_9d6b0e6b_b51f_40a8_bc9d_1418ea5356b1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumBisoxalatoborate',
        alias="class_name"
    )
    

    
    

    

    