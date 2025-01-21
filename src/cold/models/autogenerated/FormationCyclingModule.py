
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CyclingModule import Cycling







class FormationCycling(Cycling):
    """
    Class representing the `FormationCycling` entity, which inherits from:
    - Cycling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cb223440_51bd_4f16_a536_96ec408e7de4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormationCycling'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormationCycling(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cb223440_51bd_4f16_a536_96ec408e7de4',
    
    class_name='FormationCycling',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cb223440_51bd_4f16_a536_96ec408e7de4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormationCycling',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    