
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GraphicalModule import Graphical







class Representation(Graphical):
    """
    Class representing the `Representation` entity, which inherits from:
    - Graphical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb7de1a1_c30e_4f0d_94c6_fe70414d7e61'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Representation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Representation(
    
    class_iri='https://w3id.org/emmo#EMMO_eb7de1a1_c30e_4f0d_94c6_fe70414d7e61',
    
    class_name='Representation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb7de1a1_c30e_4f0d_94c6_fe70414d7e61',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Representation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    