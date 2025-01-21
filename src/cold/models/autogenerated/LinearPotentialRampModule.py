
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class LinearPotentialRamp(ElectricPotentialSignal):
    """
    Class representing the `LinearPotentialRamp` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_29f2a35a_8c09_429d_b9e8_33f3e1fc3671'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LinearPotentialRamp'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LinearPotentialRamp(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_29f2a35a_8c09_429d_b9e8_33f3e1fc3671',
    
    class_name='LinearPotentialRamp',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_29f2a35a_8c09_429d_b9e8_33f3e1fc3671',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LinearPotentialRamp',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    