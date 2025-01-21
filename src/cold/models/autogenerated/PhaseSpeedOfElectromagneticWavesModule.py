
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpeedModule import Speed



from .ElectromagneticQuantityModule import ElectromagneticQuantity







class PhaseSpeedOfElectromagneticWaves(Speed, ElectromagneticQuantity):
    """
    Class representing the `PhaseSpeedOfElectromagneticWaves` entity, which inherits from:
    - Speed, ElectromagneticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9b9e0029_8b16_4382_bd47_571a7ae7d6f6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhaseSpeedOfElectromagneticWaves'`
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
    obj = PhaseSpeedOfElectromagneticWaves(
    
    class_iri='https://w3id.org/emmo#EMMO_9b9e0029_8b16_4382_bd47_571a7ae7d6f6',
    
    class_name='PhaseSpeedOfElectromagneticWaves',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9b9e0029_8b16_4382_bd47_571a7ae7d6f6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhaseSpeedOfElectromagneticWaves',
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
    

    
    

    

    