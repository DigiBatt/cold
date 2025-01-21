
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReactionOverpotentialModule import ReactionOverpotential







class AnodicOverpotential(ReactionOverpotential):
    """
    Class representing the `AnodicOverpotential` entity, which inherits from:
    - ReactionOverpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_565c0b10_70fe_441a_b76a_b9a8e08ca7b7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnodicOverpotential'`
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
    obj = AnodicOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_565c0b10_70fe_441a_b76a_b9a8e08ca7b7',
    
    class_name='AnodicOverpotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_565c0b10_70fe_441a_b76a_b9a8e08ca7b7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnodicOverpotential',
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
    

    
    

    

    