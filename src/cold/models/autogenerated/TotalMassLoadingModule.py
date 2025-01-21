
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassLoadingModule import MassLoading







class TotalMassLoading(MassLoading):
    """
    Class representing the `TotalMassLoading` entity, which inherits from:
    - MassLoading

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8541f8b7_c55e_452d_b3f8_db29dcb2a61d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TotalMassLoading'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TotalMassLoading(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8541f8b7_c55e_452d_b3f8_db29dcb2a61d',
    
    class_name='TotalMassLoading',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8541f8b7_c55e_452d_b3f8_db29dcb2a61d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TotalMassLoading',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    