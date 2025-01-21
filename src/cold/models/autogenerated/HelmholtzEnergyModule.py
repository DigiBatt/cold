
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EnergyModule import Energy



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity







class HelmholtzEnergy(Energy, ThermodynamicalQuantity):
    """
    Class representing the `HelmholtzEnergy` entity, which inherits from:
    - Energy, ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_262d4582_15b9_4685_b693_24f8e9ead98d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HelmholtzEnergy'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HelmholtzEnergy(
    
    class_iri='https://w3id.org/emmo#EMMO_262d4582_15b9_4685_b693_24f8e9ead98d',
    
    class_name='HelmholtzEnergy',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_262d4582_15b9_4685_b693_24f8e9ead98d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HelmholtzEnergy',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    