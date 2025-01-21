
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolventModule import Solvent







class AproticSolventCompound(Solvent):
    """
    Class representing the `AproticSolventCompound` entity, which inherits from:
    - Solvent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_7fd3843d_f0b7_4490_bcf3_519fb9e2b150'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AproticSolventCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AproticSolventCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_7fd3843d_f0b7_4490_bcf3_519fb9e2b150',
    
    class_name='AproticSolventCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_7fd3843d_f0b7_4490_bcf3_519fb9e2b150',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AproticSolventCompound',
        alias="class_name"
    )
    

    
    

    

    