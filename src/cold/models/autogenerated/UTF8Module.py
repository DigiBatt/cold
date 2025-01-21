
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolModule import Symbol







class UTF8(Symbol):
    """
    Class representing the `UTF8` entity, which inherits from:
    - Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e13b2173_1dec_4b97_9ac1_1dc4b418612a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UTF8'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UTF8(
    
    class_iri='https://w3id.org/emmo#EMMO_e13b2173_1dec_4b97_9ac1_1dc4b418612a',
    
    class_name='UTF8',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e13b2173_1dec_4b97_9ac1_1dc4b418612a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UTF8',
        alias="class_name"
    )
    

    
    

    

    