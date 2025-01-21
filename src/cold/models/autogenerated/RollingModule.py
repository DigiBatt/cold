
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompressiveFormingModule import CompressiveForming







class Rolling(CompressiveForming):
    """
    Class representing the `Rolling` entity, which inherits from:
    - CompressiveForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_91c2db4b_83e2_4c36_aadf_453acc72e6d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Rolling'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Rolling(
    
    class_iri='https://w3id.org/emmo#EMMO_91c2db4b_83e2_4c36_aadf_453acc72e6d2',
    
    class_name='Rolling',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_91c2db4b_83e2_4c36_aadf_453acc72e6d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Rolling',
        alias="class_name"
    )
    

    
    

    

    