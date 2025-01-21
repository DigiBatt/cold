
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparatorModule import Separator







class GlassFibreSeparator(Separator):
    """
    Class representing the `GlassFibreSeparator` entity, which inherits from:
    - Separator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d11b0e66_c35b_4da7_80a1_037ce89b77fb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GlassFibreSeparator'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GlassFibreSeparator(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d11b0e66_c35b_4da7_80a1_037ce89b77fb',
    
    class_name='GlassFibreSeparator',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d11b0e66_c35b_4da7_80a1_037ce89b77fb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GlassFibreSeparator',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    