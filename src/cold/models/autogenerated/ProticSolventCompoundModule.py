
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolventModule import Solvent







class ProticSolventCompound(Solvent):
    """
    Class representing the `ProticSolventCompound` entity, which inherits from:
    - Solvent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_878a0e2f_12ba_484e_8197_75e57139d207'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProticSolventCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProticSolventCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_878a0e2f_12ba_484e_8197_75e57139d207',
    
    class_name='ProticSolventCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_878a0e2f_12ba_484e_8197_75e57139d207',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProticSolventCompound',
        alias="class_name"
    )
    

    
    

    

    