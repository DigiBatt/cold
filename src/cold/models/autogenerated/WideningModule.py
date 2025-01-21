
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TensileFormingModule import TensileForming







class Widening(TensileForming):
    """
    Class representing the `Widening` entity, which inherits from:
    - TensileForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_214e9a99_58de_40e2_86cf_fa6aa1d180a8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Widening'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Widening(
    
    class_iri='https://w3id.org/emmo#EMMO_214e9a99_58de_40e2_86cf_fa6aa1d180a8',
    
    class_name='Widening',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_214e9a99_58de_40e2_86cf_fa6aa1d180a8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Widening',
        alias="class_name"
    )
    

    
    

    

    