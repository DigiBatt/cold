
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IonActivityModule import IonActivity







class POH(IonActivity):
    """
    Class representing the `POH` entity, which inherits from:
    - IonActivity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3b586409_b05e_4129_ab40_93768eef503f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'POH'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = POH(
    
    class_iri='https://w3id.org/emmo#EMMO_3b586409_b05e_4129_ab40_93768eef503f',
    
    class_name='POH',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3b586409_b05e_4129_ab40_93768eef503f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'POH',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    