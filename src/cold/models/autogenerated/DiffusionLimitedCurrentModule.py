
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiffusionCurrentModule import DiffusionCurrent







class DiffusionLimitedCurrent(DiffusionCurrent):
    """
    Class representing the `DiffusionLimitedCurrent` entity, which inherits from:
    - DiffusionCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5fb7a03f_d6dd_47ee_9317_0629681c7d00'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DiffusionLimitedCurrent'`
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
    obj = DiffusionLimitedCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5fb7a03f_d6dd_47ee_9317_0629681c7d00',
    
    class_name='DiffusionLimitedCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5fb7a03f_d6dd_47ee_9317_0629681c7d00',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DiffusionLimitedCurrent',
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
    

    
    

    

    