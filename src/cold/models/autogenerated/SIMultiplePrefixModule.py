
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIPrefixModule import SIPrefix







class SIMultiplePrefix(SIPrefix):
    """
    Class representing the `SIMultiplePrefix` entity, which inherits from:
    - SIPrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2374896c_4ef8_4b3d_8c0c_0d29ba66bcfb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIMultiplePrefix'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIMultiplePrefix(
    
    class_iri='https://w3id.org/emmo#EMMO_2374896c_4ef8_4b3d_8c0c_0d29ba66bcfb',
    
    class_name='SIMultiplePrefix',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2374896c_4ef8_4b3d_8c0c_0d29ba66bcfb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIMultiplePrefix',
        alias="class_name"
    )
    

    
    

    

    