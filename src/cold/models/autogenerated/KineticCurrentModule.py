
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FaradaicCurrentModule import FaradaicCurrent







class KineticCurrent(FaradaicCurrent):
    """
    Class representing the `KineticCurrent` entity, which inherits from:
    - FaradaicCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_98b6e9d7_d5df_46a5_87dd_79642b8b2e4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KineticCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KineticCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_98b6e9d7_d5df_46a5_87dd_79642b8b2e4b',
    
    class_name='KineticCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_98b6e9d7_d5df_46a5_87dd_79642b8b2e4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'KineticCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    