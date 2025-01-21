
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProgramModule import Program



from .SoftwareModule import Software







class ApplicationProgram(Program, Software):
    """
    Class representing the `ApplicationProgram` entity, which inherits from:
    - Program, Software

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3b031fa9_8623_4ea5_8b57_bcafb70c5c8b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ApplicationProgram'`
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
    obj = ApplicationProgram(
    
    class_iri='https://w3id.org/emmo#EMMO_3b031fa9_8623_4ea5_8b57_bcafb70c5c8b',
    
    class_name='ApplicationProgram',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3b031fa9_8623_4ea5_8b57_bcafb70c5c8b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ApplicationProgram',
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
    

    
    

    

    