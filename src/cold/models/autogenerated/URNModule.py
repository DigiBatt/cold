
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .URIModule import URI







class URN(URI):
    """
    Class representing the `URN` entity, which inherits from:
    - URI

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_db99b1e5_2f34_467b_a784_d104946d9f00'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'URN'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = URN(
    
    class_iri='https://w3id.org/emmo#EMMO_db99b1e5_2f34_467b_a784_d104946d9f00',
    
    class_name='URN',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_db99b1e5_2f34_467b_a784_d104946d9f00',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'URN',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    