
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VisualModule import Visual







class Geometrical(Visual):
    """
    Class representing the `Geometrical` entity, which inherits from:
    - Visual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b5957cef_a287_442d_a3ce_fd39f20ba1cd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Geometrical'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Geometrical(
    
    class_iri='https://w3id.org/emmo#EMMO_b5957cef_a287_442d_a3ce_fd39f20ba1cd',
    
    class_name='Geometrical',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b5957cef_a287_442d_a3ce_fd39f20ba1cd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Geometrical',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    