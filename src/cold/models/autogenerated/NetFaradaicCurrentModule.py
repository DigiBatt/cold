
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FaradaicCurrentModule import FaradaicCurrent







class NetFaradaicCurrent(FaradaicCurrent):
    """
    Class representing the `NetFaradaicCurrent` entity, which inherits from:
    - FaradaicCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_14577b99_a8a9_4358_9bc5_ab8c401dd34b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NetFaradaicCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NetFaradaicCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_14577b99_a8a9_4358_9bc5_ab8c401dd34b',
    
    class_name='NetFaradaicCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_14577b99_a8a9_4358_9bc5_ab8c401dd34b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NetFaradaicCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    