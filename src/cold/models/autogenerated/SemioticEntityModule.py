
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticsModule import Semiotics







class SemioticEntity(Semiotics):
    """
    Class representing the `SemioticEntity` entity, which inherits from:
    - Semiotics

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b803f122_4acb_4064_9d71_c1e5fd091fc9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SemioticEntity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SemioticEntity(
    
    class_iri='https://w3id.org/emmo#EMMO_b803f122_4acb_4064_9d71_c1e5fd091fc9',
    
    class_name='SemioticEntity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b803f122_4acb_4064_9d71_c1e5fd091fc9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SemioticEntity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    