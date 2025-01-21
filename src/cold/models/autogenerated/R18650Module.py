
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CylindricalCaseModule import CylindricalCase







class R18650(CylindricalCase):
    """
    Class representing the `R18650` entity, which inherits from:
    - CylindricalCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3d2f9945_2319_4a08_899b_6a5ffabd4925'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R18650'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R18650(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3d2f9945_2319_4a08_899b_6a5ffabd4925',
    
    class_name='R18650',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3d2f9945_2319_4a08_899b_6a5ffabd4925',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R18650',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    