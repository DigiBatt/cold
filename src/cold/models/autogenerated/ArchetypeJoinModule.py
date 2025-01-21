
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class ArchetypeJoin(JoinManufacturing):
    """
    Class representing the `ArchetypeJoin` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_22496460_c849_4bd7_8be0_9a1202506f18'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ArchetypeJoin'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ArchetypeJoin(
    
    class_iri='https://w3id.org/emmo#EMMO_22496460_c849_4bd7_8be0_9a1202506f18',
    
    class_name='ArchetypeJoin',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_22496460_c849_4bd7_8be0_9a1202506f18',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ArchetypeJoin',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    