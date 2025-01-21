
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalModule import Fundamental







class TemporallyFundamental(Fundamental):
    """
    Class representing the `TemporallyFundamental` entity, which inherits from:
    - Fundamental

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aaad78a9_abaf_4f97_9c1a_d763a94c4ba3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemporallyFundamental'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemporallyFundamental(
    
    class_iri='https://w3id.org/emmo#EMMO_aaad78a9_abaf_4f97_9c1a_d763a94c4ba3',
    
    class_name='TemporallyFundamental',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aaad78a9_abaf_4f97_9c1a_d763a94c4ba3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemporallyFundamental',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    