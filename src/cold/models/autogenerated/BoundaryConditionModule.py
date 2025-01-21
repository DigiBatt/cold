
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ControlPropertyModule import ControlProperty







class BoundaryCondition(ControlProperty):
    """
    Class representing the `BoundaryCondition` entity, which inherits from:
    - ControlProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f2f36f22_3738_49dd_b43b_7469db6675df'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BoundaryCondition'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BoundaryCondition(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f2f36f22_3738_49dd_b43b_7469db6675df',
    
    class_name='BoundaryCondition',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f2f36f22_3738_49dd_b43b_7469db6675df',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BoundaryCondition',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    