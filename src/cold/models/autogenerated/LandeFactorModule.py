
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GFactorModule import GFactor



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity







class LandeFactor(GFactor, AtomicAndNuclearPhysicsQuantity):
    """
    Class representing the `LandeFactor` entity, which inherits from:
    - GFactor, AtomicAndNuclearPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2c33f59a_fbeb_445e_aea9_8b05738b5f8b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LandeFactor'`
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
    obj = LandeFactor(
    
    class_iri='https://w3id.org/emmo#EMMO_2c33f59a_fbeb_445e_aea9_8b05738b5f8b',
    
    class_name='LandeFactor',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2c33f59a_fbeb_445e_aea9_8b05738b5f8b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LandeFactor',
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
    

    
    

    

    