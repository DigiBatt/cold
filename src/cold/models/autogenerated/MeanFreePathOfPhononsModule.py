
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeanFreePathModule import MeanFreePath



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class MeanFreePathOfPhonons(MeanFreePath, CondensedMatterPhysicsQuantity):
    """
    Class representing the `MeanFreePathOfPhonons` entity, which inherits from:
    - MeanFreePath, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8dacb56f_5931_443b_8de6_f31aec44036c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeanFreePathOfPhonons'`
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
    obj = MeanFreePathOfPhonons(
    
    class_iri='https://w3id.org/emmo#EMMO_8dacb56f_5931_443b_8de6_f31aec44036c',
    
    class_name='MeanFreePathOfPhonons',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8dacb56f_5931_443b_8de6_f31aec44036c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeanFreePathOfPhonons',
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
    

    
    

    

    