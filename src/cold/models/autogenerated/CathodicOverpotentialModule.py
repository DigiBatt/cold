
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReactionOverpotentialModule import ReactionOverpotential







class CathodicOverpotential(ReactionOverpotential):
    """
    Class representing the `CathodicOverpotential` entity, which inherits from:
    - ReactionOverpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0853b072_3b80_4864_8147_24ce35407ade'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CathodicOverpotential'`
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
    obj = CathodicOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0853b072_3b80_4864_8147_24ce35407ade',
    
    class_name='CathodicOverpotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0853b072_3b80_4864_8147_24ce35407ade',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CathodicOverpotential',
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
    

    
    

    

    