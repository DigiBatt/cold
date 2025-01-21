
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodeReactionModule import ElectrodeReaction



from .DissolutionModule import Dissolution







class Electrodissolution(ElectrodeReaction, Dissolution):
    """
    Class representing the `Electrodissolution` entity, which inherits from:
    - ElectrodeReaction, Dissolution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4df84ec1_8a1a_4770_963f_bf48009bd043'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrodissolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrodissolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4df84ec1_8a1a_4770_963f_bf48009bd043',
    
    class_name='Electrodissolution',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4df84ec1_8a1a_4770_963f_bf48009bd043',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrodissolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    