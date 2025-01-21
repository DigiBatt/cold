
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class AverageLogarithmicEnergyDecrement(AtomicAndNuclearPhysicsQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `AverageLogarithmicEnergyDecrement` entity, which inherits from:
    - AtomicAndNuclearPhysicsQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_44afb828_82bf_4091_a7a0_7c80ec47281d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AverageLogarithmicEnergyDecrement'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AverageLogarithmicEnergyDecrement(
    
    class_iri='https://w3id.org/emmo#EMMO_44afb828_82bf_4091_a7a0_7c80ec47281d',
    
    class_name='AverageLogarithmicEnergyDecrement',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_44afb828_82bf_4091_a7a0_7c80ec47281d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AverageLogarithmicEnergyDecrement',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    