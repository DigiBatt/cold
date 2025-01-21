
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class PackingFraction(AtomicAndNuclearPhysicsQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `PackingFraction` entity, which inherits from:
    - AtomicAndNuclearPhysicsQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9f33b66d_f2d6_47d0_b163_deeb3d45685a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PackingFraction'`
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
    obj = PackingFraction(
    
    class_iri='https://w3id.org/emmo#EMMO_9f33b66d_f2d6_47d0_b163_deeb3d45685a',
    
    class_name='PackingFraction',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9f33b66d_f2d6_47d0_b163_deeb3d45685a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PackingFraction',
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
    

    
    

    

    