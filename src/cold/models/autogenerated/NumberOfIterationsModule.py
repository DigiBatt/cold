
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity







class NumberOfIterations(PureNumberQuantity):
    """
    Class representing the `NumberOfIterations` entity, which inherits from:
    - PureNumberQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_88dd2bce_fb17_4705_905d_892681812290'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfIterations'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfIterations(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_88dd2bce_fb17_4705_905d_892681812290',
    
    class_name='NumberOfIterations',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_88dd2bce_fb17_4705_905d_892681812290',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfIterations',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    