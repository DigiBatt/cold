
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SubstanceModule import Substance







class ContinuumSubstance(Substance):
    """
    Class representing the `ContinuumSubstance` entity, which inherits from:
    - Substance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8b0923ab_b500_477b_9ce9_8b3a3e4dc4f2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ContinuumSubstance'`
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
    obj = ContinuumSubstance(
    
    class_iri='https://w3id.org/emmo#EMMO_8b0923ab_b500_477b_9ce9_8b3a3e4dc4f2',
    
    class_name='ContinuumSubstance',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8b0923ab_b500_477b_9ce9_8b3a3e4dc4f2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ContinuumSubstance',
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
    

    
    

    

    