
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecificCapacityModule import SpecificCapacity







class DischargingSpecificCapacity(SpecificCapacity):
    """
    Class representing the `DischargingSpecificCapacity` entity, which inherits from:
    - SpecificCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_884650fd_6cc6_4ec6_8264_c18fbe6b90ee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DischargingSpecificCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DischargingSpecificCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_884650fd_6cc6_4ec6_8264_c18fbe6b90ee',
    
    class_name='DischargingSpecificCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_884650fd_6cc6_4ec6_8264_c18fbe6b90ee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DischargingSpecificCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    