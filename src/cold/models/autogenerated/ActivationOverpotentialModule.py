
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OverpotentialModule import Overpotential







class ActivationOverpotential(Overpotential):
    """
    Class representing the `ActivationOverpotential` entity, which inherits from:
    - Overpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fa406b0_512a_4d59_9e0c_5d8aba0103ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivationOverpotential'`
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
    obj = ActivationOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fa406b0_512a_4d59_9e0c_5d8aba0103ae',
    
    class_name='ActivationOverpotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fa406b0_512a_4d59_9e0c_5d8aba0103ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivationOverpotential',
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
    

    
    

    

    