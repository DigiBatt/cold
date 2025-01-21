
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TensileFormingModule import TensileForming







class DrawForming(TensileForming):
    """
    Class representing the `DrawForming` entity, which inherits from:
    - TensileForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_01048432_3722_40a9_aa37_ea009da44272'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DrawForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DrawForming(
    
    class_iri='https://w3id.org/emmo#EMMO_01048432_3722_40a9_aa37_ea009da44272',
    
    class_name='DrawForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_01048432_3722_40a9_aa37_ea009da44272',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DrawForming',
        alias="class_name"
    )
    

    
    

    

    