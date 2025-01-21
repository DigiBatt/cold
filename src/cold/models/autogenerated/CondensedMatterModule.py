
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StateOfMatterModule import StateOfMatter







class CondensedMatter(StateOfMatter):
    """
    Class representing the `CondensedMatter` entity, which inherits from:
    - StateOfMatter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_220b7201_d277_4dca_bf6a_5a5e2c4062dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CondensedMatter'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CondensedMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_220b7201_d277_4dca_bf6a_5a5e2c4062dd',
    
    class_name='CondensedMatter',
    
    conceptualisation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_220b7201_d277_4dca_bf6a_5a5e2c4062dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CondensedMatter',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    

    
    

    

    