
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerspectiveModule import Perspective







class Persistence(Perspective):
    """
    Class representing the `Persistence` entity, which inherits from:
    - Perspective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e04884d9_eda6_487e_93d5_7722d7eda96b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Persistence'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Persistence(
    
    class_iri='https://w3id.org/emmo#EMMO_e04884d9_eda6_487e_93d5_7722d7eda96b',
    
    class_name='Persistence',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e04884d9_eda6_487e_93d5_7722d7eda96b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Persistence',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    