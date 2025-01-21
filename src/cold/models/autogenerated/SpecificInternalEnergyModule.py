
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecificEnergyModule import SpecificEnergy







class SpecificInternalEnergy(SpecificEnergy):
    """
    Class representing the `SpecificInternalEnergy` entity, which inherits from:
    - SpecificEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e86c84bd_af21_402d_a1ad_42a90599f9eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpecificInternalEnergy'`
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
    obj = SpecificInternalEnergy(
    
    class_iri='https://w3id.org/emmo#EMMO_e86c84bd_af21_402d_a1ad_42a90599f9eb',
    
    class_name='SpecificInternalEnergy',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e86c84bd_af21_402d_a1ad_42a90599f9eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpecificInternalEnergy',
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
    

    
    

    

    