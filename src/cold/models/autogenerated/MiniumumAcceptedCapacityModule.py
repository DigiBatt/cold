
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatedCapacityModule import RatedCapacity







class MiniumumAcceptedCapacity(RatedCapacity):
    """
    Class representing the `MiniumumAcceptedCapacity` entity, which inherits from:
    - RatedCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d3c0078e_c1d3_461e_873d_e5c3adf441c5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MiniumumAcceptedCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MiniumumAcceptedCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d3c0078e_c1d3_461e_873d_e5c3adf441c5',
    
    class_name='MiniumumAcceptedCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d3c0078e_c1d3_461e_873d_e5c3adf441c5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MiniumumAcceptedCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    