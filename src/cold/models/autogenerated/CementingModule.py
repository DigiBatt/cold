
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ArchetypeJoinModule import ArchetypeJoin







class Cementing(ArchetypeJoin):
    """
    Class representing the `Cementing` entity, which inherits from:
    - ArchetypeJoin

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dc3a6b2d_e31d_491a_ab40_c433f8dd8d48'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cementing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Cementing(
    
    class_iri='https://w3id.org/emmo#EMMO_dc3a6b2d_e31d_491a_ab40_c433f8dd8d48',
    
    class_name='Cementing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dc3a6b2d_e31d_491a_ab40_c433f8dd8d48',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cementing',
        alias="class_name"
    )
    

    
    

    

    