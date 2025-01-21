
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompressiveFormingModule import CompressiveForming







class FreeForming(CompressiveForming):
    """
    Class representing the `FreeForming` entity, which inherits from:
    - CompressiveForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7432b843_cfd2_4345_a3d2_eaa539b27e61'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FreeForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FreeForming(
    
    class_iri='https://w3id.org/emmo#EMMO_7432b843_cfd2_4345_a3d2_eaa539b27e61',
    
    class_name='FreeForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7432b843_cfd2_4345_a3d2_eaa539b27e61',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FreeForming',
        alias="class_name"
    )
    

    
    

    

    