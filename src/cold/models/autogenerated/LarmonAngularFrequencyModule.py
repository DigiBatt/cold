
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity



from .AngularFrequencyModule import AngularFrequency







class LarmonAngularFrequency(AtomicAndNuclearPhysicsQuantity, AngularFrequency):
    """
    Class representing the `LarmonAngularFrequency` entity, which inherits from:
    - AtomicAndNuclearPhysicsQuantity, AngularFrequency

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b452fe23_0c61_436d_8357_57a521448801'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LarmonAngularFrequency'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LarmonAngularFrequency(
    
    class_iri='https://w3id.org/emmo#EMMO_b452fe23_0c61_436d_8357_57a521448801',
    
    class_name='LarmonAngularFrequency',
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b452fe23_0c61_436d_8357_57a521448801',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LarmonAngularFrequency',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    