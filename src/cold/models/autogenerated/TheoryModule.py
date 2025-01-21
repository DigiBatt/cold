
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DescriptionModule import Description







class Theory(Description):
    """
    Class representing the `Theory` entity, which inherits from:
    - Description

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8d2d9374_ef3a_47e6_8595_6bc208e07519'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Theory'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Theory(
    
    class_iri='https://w3id.org/emmo#EMMO_8d2d9374_ef3a_47e6_8595_6bc208e07519',
    
    class_name='Theory',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8d2d9374_ef3a_47e6_8595_6bc208e07519',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Theory',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    