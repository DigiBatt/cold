
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingJoinModule import FormingJoin







class Folding(FormingJoin):
    """
    Class representing the `Folding` entity, which inherits from:
    - FormingJoin

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aa446897_0683_4e9b_9b0e_b6081d2d70d8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Folding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Folding(
    
    class_iri='https://w3id.org/emmo#EMMO_aa446897_0683_4e9b_9b0e_b6081d2d70d8',
    
    class_name='Folding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aa446897_0683_4e9b_9b0e_b6081d2d70d8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Folding',
        alias="class_name"
    )
    

    
    

    

    