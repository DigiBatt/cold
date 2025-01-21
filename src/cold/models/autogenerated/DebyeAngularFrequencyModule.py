
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity



from .AngularFrequencyModule import AngularFrequency







class DebyeAngularFrequency(CondensedMatterPhysicsQuantity, AngularFrequency):
    """
    Class representing the `DebyeAngularFrequency` entity, which inherits from:
    - CondensedMatterPhysicsQuantity, AngularFrequency

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_65ec122c_b67f_4009_8b16_2df7dfae118a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DebyeAngularFrequency'`
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
    obj = DebyeAngularFrequency(
    
    class_iri='https://w3id.org/emmo#EMMO_65ec122c_b67f_4009_8b16_2df7dfae118a',
    
    class_name='DebyeAngularFrequency',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_65ec122c_b67f_4009_8b16_2df7dfae118a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DebyeAngularFrequency',
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
    

    
    

    

    