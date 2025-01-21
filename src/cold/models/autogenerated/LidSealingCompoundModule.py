
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompositePhysicalObjectModule import CompositePhysicalObject







class LidSealingCompound(CompositePhysicalObject):
    """
    Class representing the `LidSealingCompound` entity, which inherits from:
    - CompositePhysicalObject

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6559c04d_75bc_41ea_8ed8_8d3c09dae6b0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LidSealingCompound'`
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
    obj = LidSealingCompound(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6559c04d_75bc_41ea_8ed8_8d3c09dae6b0',
    
    class_name='LidSealingCompound',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6559c04d_75bc_41ea_8ed8_8d3c09dae6b0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LidSealingCompound',
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
    

    
    

    

    