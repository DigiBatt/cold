
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class AtomicAndNuclearPhysicsQuantity(ISO80000Categorised):
    """
    Class representing the `AtomicAndNuclearPhysicsQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3b1b64d1_60c9_4689_a300_eb9cd56e368b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AtomicAndNuclearPhysicsQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AtomicAndNuclearPhysicsQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_3b1b64d1_60c9_4689_a300_eb9cd56e368b',
    
    class_name='AtomicAndNuclearPhysicsQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3b1b64d1_60c9_4689_a300_eb9cd56e368b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AtomicAndNuclearPhysicsQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    