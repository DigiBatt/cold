
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeterminationModule import Determination







class Estimation(Determination):
    """
    Class representing the `Estimation` entity, which inherits from:
    - Determination

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1c0b22a2_be82_4fa8_9e2b_a569a625d442'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Estimation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Estimation(
    
    class_iri='https://w3id.org/emmo#EMMO_1c0b22a2_be82_4fa8_9e2b_a569a625d442',
    
    class_name='Estimation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1c0b22a2_be82_4fa8_9e2b_a569a625d442',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Estimation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    