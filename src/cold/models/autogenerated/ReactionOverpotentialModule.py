
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OverpotentialModule import Overpotential







class ReactionOverpotential(Overpotential):
    """
    Class representing the `ReactionOverpotential` entity, which inherits from:
    - Overpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4fadc4e_ca7d_4e4e_89cf_eacf45b4041e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReactionOverpotential'`
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
    obj = ReactionOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4fadc4e_ca7d_4e4e_89cf_eacf45b4041e',
    
    class_name='ReactionOverpotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4fadc4e_ca7d_4e4e_89cf_eacf45b4041e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReactionOverpotential',
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
    

    
    

    

    