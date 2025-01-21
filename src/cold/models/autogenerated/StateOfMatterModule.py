
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ContinuumSubstanceModule import ContinuumSubstance







class StateOfMatter(ContinuumSubstance):
    """
    Class representing the `StateOfMatter` entity, which inherits from:
    - ContinuumSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b9695e87_8261_412e_83cd_a86459426a28'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StateOfMatter'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StateOfMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_b9695e87_8261_412e_83cd_a86459426a28',
    
    class_name='StateOfMatter',
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b9695e87_8261_412e_83cd_a86459426a28',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StateOfMatter',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    