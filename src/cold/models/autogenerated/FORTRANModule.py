
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompiledLanguageModule import CompiledLanguage







class FORTRAN(CompiledLanguage):
    """
    Class representing the `FORTRAN` entity, which inherits from:
    - CompiledLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aab6a0cc_2fbd_43ac_ac5a_b7b7b75331dc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FORTRAN'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FORTRAN(
    
    class_iri='https://w3id.org/emmo#EMMO_aab6a0cc_2fbd_43ac_ac5a_b7b7b75331dc',
    
    class_name='FORTRAN',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aab6a0cc_2fbd_43ac_ac5a_b7b7b75331dc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FORTRAN',
        alias="class_name"
    )
    

    
    

    

    