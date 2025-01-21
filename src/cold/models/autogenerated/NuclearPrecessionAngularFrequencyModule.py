
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity



from .AngularFrequencyModule import AngularFrequency







class NuclearPrecessionAngularFrequency(AtomicAndNuclearPhysicsQuantity, AngularFrequency):
    """
    Class representing the `NuclearPrecessionAngularFrequency` entity, which inherits from:
    - AtomicAndNuclearPhysicsQuantity, AngularFrequency

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_953d7ce1_2a40_4391_831f_e4be15162efb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NuclearPrecessionAngularFrequency'`
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
    obj = NuclearPrecessionAngularFrequency(
    
    class_iri='https://w3id.org/emmo#EMMO_953d7ce1_2a40_4391_831f_e4be15162efb',
    
    class_name='NuclearPrecessionAngularFrequency',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_953d7ce1_2a40_4391_831f_e4be15162efb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NuclearPrecessionAngularFrequency',
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
    

    
    

    

    