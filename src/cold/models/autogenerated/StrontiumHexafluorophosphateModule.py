
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumHexafluorophosphate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumHexafluorophosphate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_3896eebe_80a4_441a_bd73_52be793482a6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumHexafluorophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumHexafluorophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_3896eebe_80a4_441a_bd73_52be793482a6',
    
    class_name='StrontiumHexafluorophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_3896eebe_80a4_441a_bd73_52be793482a6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumHexafluorophosphate',
        alias="class_name"
    )
    

    
    

    

    