
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ExactConstantModule import ExactConstant







class SIExactConstant(ExactConstant):
    """
    Class representing the `SIExactConstant` entity, which inherits from:
    - ExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f2ca6dd0_0e5f_4392_a92d_cafdae6cfc95'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIExactConstant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIExactConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_f2ca6dd0_0e5f_4392_a92d_cafdae6cfc95',
    
    class_name='SIExactConstant',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f2ca6dd0_0e5f_4392_a92d_cafdae6cfc95',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIExactConstant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    