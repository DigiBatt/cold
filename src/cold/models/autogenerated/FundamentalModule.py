
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StructuralModule import Structural







class Fundamental(Structural):
    """
    Class representing the `Fundamental` entity, which inherits from:
    - Structural

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_57c75ca1_bf8a_42bc_85d9_58cfe38c7df2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Fundamental'`
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
    obj = Fundamental(
    
    class_iri='https://w3id.org/emmo#EMMO_57c75ca1_bf8a_42bc_85d9_58cfe38c7df2',
    
    class_name='Fundamental',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_57c75ca1_bf8a_42bc_85d9_58cfe38c7df2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Fundamental',
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
    

    
    

    

    