
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent







class ElectricCurrentPhasor(ElectricCurrent):
    """
    Class representing the `ElectricCurrentPhasor` entity, which inherits from:
    - ElectricCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8ef46550_7bf2_4ef9_8334_ca3d63fb69b1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentPhasor'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentPhasor(
    
    class_iri='https://w3id.org/emmo#EMMO_8ef46550_7bf2_4ef9_8334_ca3d63fb69b1',
    
    class_name='ElectricCurrentPhasor',
    
    wikidataReference="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8ef46550_7bf2_4ef9_8334_ca3d63fb69b1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentPhasor',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    