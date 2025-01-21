
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingJoinModule import FormingJoin







class Riveting(FormingJoin):
    """
    Class representing the `Riveting` entity, which inherits from:
    - FormingJoin

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d3eecd54_e9bf_4c6f_bef8_6086cb9aa7b5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Riveting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Riveting(
    
    class_iri='https://w3id.org/emmo#EMMO_d3eecd54_e9bf_4c6f_bef8_6086cb9aa7b5',
    
    class_name='Riveting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d3eecd54_e9bf_4c6f_bef8_6086cb9aa7b5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Riveting',
        alias="class_name"
    )
    

    
    

    

    