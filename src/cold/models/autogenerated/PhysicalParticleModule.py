
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalStructureModule import CausalStructure







class PhysicalParticle(CausalStructure):
    """
    Class representing the `PhysicalParticle` entity, which inherits from:
    - CausalStructure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a15cea10_9946_4d2b_95c5_cfc333fd2abb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalParticle'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_a15cea10_9946_4d2b_95c5_cfc333fd2abb',
    
    class_name='PhysicalParticle',
    
    definition="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a15cea10_9946_4d2b_95c5_cfc333fd2abb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalParticle',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    