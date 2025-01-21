
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeterminerModule import Determiner







class Observer(Determiner):
    """
    Class representing the `Observer` entity, which inherits from:
    - Determiner

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ea67caa5_2609_4e91_98ae_81103f2d5c25'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Observer'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Observer(
    
    class_iri='https://w3id.org/emmo#EMMO_ea67caa5_2609_4e91_98ae_81103f2d5c25',
    
    class_name='Observer',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ea67caa5_2609_4e91_98ae_81103f2d5c25',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Observer',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    