
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticSystemModule import HolisticSystem







class Organisation(HolisticSystem):
    """
    Class representing the `Organisation` entity, which inherits from:
    - HolisticSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c0f72631_d7c2_434c_9c26_5c44123df682'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Organisation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Organisation(
    
    class_iri='https://w3id.org/emmo#EMMO_c0f72631_d7c2_434c_9c26_5c44123df682',
    
    class_name='Organisation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c0f72631_d7c2_434c_9c26_5c44123df682',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Organisation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    