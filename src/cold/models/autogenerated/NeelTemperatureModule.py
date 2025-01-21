
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CriticalTemperatureModule import CriticalTemperature



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class NeelTemperature(CriticalTemperature, CondensedMatterPhysicsQuantity):
    """
    Class representing the `NeelTemperature` entity, which inherits from:
    - CriticalTemperature, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f0b8bace_151e_4f54_8129_c180fd83ae44'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NeelTemperature'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NeelTemperature(
    
    class_iri='https://w3id.org/emmo#EMMO_f0b8bace_151e_4f54_8129_c180fd83ae44',
    
    class_name='NeelTemperature',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f0b8bace_151e_4f54_8129_c180fd83ae44',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NeelTemperature',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    