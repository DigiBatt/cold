
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ContinuumSubstanceModule import ContinuumSubstance







class PhaseOfMatter(ContinuumSubstance):
    """
    Class representing the `PhaseOfMatter` entity, which inherits from:
    - ContinuumSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_668fbd5b_6f1b_405c_9c6b_d6067bd0595a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhaseOfMatter'`
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
    obj = PhaseOfMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_668fbd5b_6f1b_405c_9c6b_d6067bd0595a',
    
    class_name='PhaseOfMatter',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_668fbd5b_6f1b_405c_9c6b_d6067bd0595a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhaseOfMatter',
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
    

    
    

    

    