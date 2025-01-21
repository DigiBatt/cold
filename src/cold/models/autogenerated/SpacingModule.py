
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolModule import Symbol







class Spacing(Symbol):
    """
    Class representing the `Spacing` entity, which inherits from:
    - Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_432192c4_111f_4e80_b7cd_c6ce1c1129ea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Spacing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Spacing(
    
    class_iri='https://w3id.org/emmo#EMMO_432192c4_111f_4e80_b7cd_c6ce1c1129ea',
    
    class_name='Spacing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_432192c4_111f_4e80_b7cd_c6ce1c1129ea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Spacing',
        alias="class_name"
    )
    

    
    

    

    