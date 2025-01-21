
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DisplacementModule import Displacement



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class DisplacementVector(Displacement, CondensedMatterPhysicsQuantity):
    """
    Class representing the `DisplacementVector` entity, which inherits from:
    - Displacement, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c5fcfb08_12a9_4030_925b_14e3a0eabd07'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DisplacementVector'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DisplacementVector(
    
    class_iri='https://w3id.org/emmo#EMMO_c5fcfb08_12a9_4030_925b_14e3a0eabd07',
    
    class_name='DisplacementVector',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c5fcfb08_12a9_4030_925b_14e3a0eabd07',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DisplacementVector',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    