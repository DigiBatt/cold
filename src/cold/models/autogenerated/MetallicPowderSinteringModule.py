
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class MetallicPowderSintering(Sintering):
    """
    Class representing the `MetallicPowderSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1a9e6e27_1e1d_492a_824e_6fb848574846'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetallicPowderSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetallicPowderSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_1a9e6e27_1e1d_492a_824e_6fb848574846',
    
    class_name='MetallicPowderSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1a9e6e27_1e1d_492a_824e_6fb848574846',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetallicPowderSintering',
        alias="class_name"
    )
    

    
    

    

    