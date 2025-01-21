
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class FirstGenerationFermion(FundamentalFermion):
    """
    Class representing the `FirstGenerationFermion` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7773f63a_cd7c_4393_b36b_cd1b8a71565a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FirstGenerationFermion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FirstGenerationFermion(
    
    class_iri='https://w3id.org/emmo#EMMO_7773f63a_cd7c_4393_b36b_cd1b8a71565a',
    
    class_name='FirstGenerationFermion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7773f63a_cd7c_4393_b36b_cd1b8a71565a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FirstGenerationFermion',
        alias="class_name"
    )
    

    
    

    

    