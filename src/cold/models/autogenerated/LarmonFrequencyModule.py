
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity



from .FrequencyModule import Frequency







class LarmonFrequency(AtomicAndNuclearPhysicsQuantity, Frequency):
    """
    Class representing the `LarmonFrequency` entity, which inherits from:
    - AtomicAndNuclearPhysicsQuantity, Frequency

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_40923aa2_c600_44e4_8af8_80260ba25ab2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LarmonFrequency'`
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
    obj = LarmonFrequency(
    
    class_iri='https://w3id.org/emmo#EMMO_40923aa2_c600_44e4_8af8_80260ba25ab2',
    
    class_name='LarmonFrequency',
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_40923aa2_c600_44e4_8af8_80260ba25ab2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LarmonFrequency',
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
    

    
    

    

    