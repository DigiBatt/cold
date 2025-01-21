
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class ThirdGenerationFermion(FundamentalFermion):
    """
    Class representing the `ThirdGenerationFermion` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_82d6c4b3_a037_49de_9622_0407af40bdeb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThirdGenerationFermion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThirdGenerationFermion(
    
    class_iri='https://w3id.org/emmo#EMMO_82d6c4b3_a037_49de_9622_0407af40bdeb',
    
    class_name='ThirdGenerationFermion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_82d6c4b3_a037_49de_9622_0407af40bdeb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThirdGenerationFermion',
        alias="class_name"
    )
    

    
    

    

    