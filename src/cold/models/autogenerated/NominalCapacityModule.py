
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatedCapacityModule import RatedCapacity







class NominalCapacity(RatedCapacity):
    """
    Class representing the `NominalCapacity` entity, which inherits from:
    - RatedCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8abde9d0_84f6_4b4f_a87e_86028a397100'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NominalCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NominalCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8abde9d0_84f6_4b4f_a87e_86028a397100',
    
    class_name='NominalCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8abde9d0_84f6_4b4f_a87e_86028a397100',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NominalCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    