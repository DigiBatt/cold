
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RadiusModule import Radius



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity







class ElectronRadius(Radius, AtomicAndNuclearPhysicsQuantity):
    """
    Class representing the `ElectronRadius` entity, which inherits from:
    - Radius, AtomicAndNuclearPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e6a173ac_40e9_4616_8883_710b358f5c85'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronRadius'`
        - **Alias**: `class_name`
    
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
    obj = ElectronRadius(
    
    class_iri='https://w3id.org/emmo#EMMO_e6a173ac_40e9_4616_8883_710b358f5c85',
    
    class_name='ElectronRadius',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e6a173ac_40e9_4616_8883_710b358f5c85',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronRadius',
        alias="class_name"
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
    

    
    

    

    