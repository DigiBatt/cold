
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HardeningByFormingModule import HardeningByForming







class HardeningByForging(HardeningByForming):
    """
    Class representing the `HardeningByForging` entity, which inherits from:
    - HardeningByForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c62b76d5_c1cc_432a_8c9e_7684ab054669'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardeningByForging'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardeningByForging(
    
    class_iri='https://w3id.org/emmo#EMMO_c62b76d5_c1cc_432a_8c9e_7684ab054669',
    
    class_name='HardeningByForging',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c62b76d5_c1cc_432a_8c9e_7684ab054669',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardeningByForging',
        alias="class_name"
    )
    

    
    

    

    