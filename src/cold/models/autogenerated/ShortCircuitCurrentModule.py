
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellCurrentModule import CellCurrent







class ShortCircuitCurrent(CellCurrent):
    """
    Class representing the `ShortCircuitCurrent` entity, which inherits from:
    - CellCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_75c28dc8_3d7d_4b6e_861e_6c8b1ad7d644'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ShortCircuitCurrent'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ShortCircuitCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_75c28dc8_3d7d_4b6e_861e_6c8b1ad7d644',
    
    class_name='ShortCircuitCurrent',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_75c28dc8_3d7d_4b6e_861e_6c8b1ad7d644',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ShortCircuitCurrent',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    