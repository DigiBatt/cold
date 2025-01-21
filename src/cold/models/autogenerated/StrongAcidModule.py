
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AcidModule import Acid







class StrongAcid(Acid):
    """
    Class representing the `StrongAcid` entity, which inherits from:
    - Acid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_f5b930f9_2f95_4268_993c_ff6b57ae7691'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrongAcid'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrongAcid(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_f5b930f9_2f95_4268_993c_ff6b57ae7691',
    
    class_name='StrongAcid',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_f5b930f9_2f95_4268_993c_ff6b57ae7691',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrongAcid',
        alias="class_name"
    )
    

    
    

    

    