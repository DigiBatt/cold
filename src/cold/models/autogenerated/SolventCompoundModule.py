
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalCompoundModule import ChemicalCompound







class SolventCompound(ChemicalCompound):
    """
    Class representing the `SolventCompound` entity, which inherits from:
    - ChemicalCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_81b90332_8b8e_407b_a8fd_517306d56a59'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolventCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolventCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_81b90332_8b8e_407b_a8fd_517306d56a59',
    
    class_name='SolventCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_81b90332_8b8e_407b_a8fd_517306d56a59',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolventCompound',
        alias="class_name"
    )
    

    
    

    

    