
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CylindricalCaseModule import CylindricalCase







class R46800(CylindricalCase):
    """
    Class representing the `R46800` entity, which inherits from:
    - CylindricalCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1afa2c7e_6ddd_4a9b_9623_40975131a304'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R46800'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R46800(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1afa2c7e_6ddd_4a9b_9623_40975131a304',
    
    class_name='R46800',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1afa2c7e_6ddd_4a9b_9623_40975131a304',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R46800',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    