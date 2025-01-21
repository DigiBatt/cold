
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparateManufacturingModule import SeparateManufacturing







class DefinedEdgeCutting(SeparateManufacturing):
    """
    Class representing the `DefinedEdgeCutting` entity, which inherits from:
    - SeparateManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8679c7d3_fd5d_49ba_bc1f_1bb820a1f73f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DefinedEdgeCutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DefinedEdgeCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_8679c7d3_fd5d_49ba_bc1f_1bb820a1f73f',
    
    class_name='DefinedEdgeCutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8679c7d3_fd5d_49ba_bc1f_1bb820a1f73f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DefinedEdgeCutting',
        alias="class_name"
    )
    

    
    

    

    