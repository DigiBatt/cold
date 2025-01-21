
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class SecondGenerationFermion(FundamentalFermion):
    """
    Class representing the `SecondGenerationFermion` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_124c07b7_38ea_405c_81b1_5c65eee1a41a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SecondGenerationFermion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SecondGenerationFermion(
    
    class_iri='https://w3id.org/emmo#EMMO_124c07b7_38ea_405c_81b1_5c65eee1a41a',
    
    class_name='SecondGenerationFermion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_124c07b7_38ea_405c_81b1_5c65eee1a41a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SecondGenerationFermion',
        alias="class_name"
    )
    

    
    

    

    