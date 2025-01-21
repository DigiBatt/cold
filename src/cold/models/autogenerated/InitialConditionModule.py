
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ControlPropertyModule import ControlProperty







class InitialCondition(ControlProperty):
    """
    Class representing the `InitialCondition` entity, which inherits from:
    - ControlProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2c4c2626_7db5_440c_a65e_95ed2986ee01'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InitialCondition'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InitialCondition(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2c4c2626_7db5_440c_a65e_95ed2986ee01',
    
    class_name='InitialCondition',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2c4c2626_7db5_440c_a65e_95ed2986ee01',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InitialCondition',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    