
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class LiquidPhaseSintering(Sintering):
    """
    Class representing the `LiquidPhaseSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3cb27225_df45_4616_aa3b_32dba383524c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidPhaseSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidPhaseSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_3cb27225_df45_4616_aa3b_32dba383524c',
    
    class_name='LiquidPhaseSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3cb27225_df45_4616_aa3b_32dba383524c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidPhaseSintering',
        alias="class_name"
    )
    

    
    

    

    