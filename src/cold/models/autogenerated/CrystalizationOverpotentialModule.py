
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReactionOverpotentialModule import ReactionOverpotential







class CrystalizationOverpotential(ReactionOverpotential):
    """
    Class representing the `CrystalizationOverpotential` entity, which inherits from:
    - ReactionOverpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8de9735b_374a_4a0f_b29f_71a50794cf94'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CrystalizationOverpotential'`
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
    obj = CrystalizationOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8de9735b_374a_4a0f_b29f_71a50794cf94',
    
    class_name='CrystalizationOverpotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8de9735b_374a_4a0f_b29f_71a50794cf94',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CrystalizationOverpotential',
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
    

    
    

    

    