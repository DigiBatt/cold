
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagneticFluxDensityModule import MagneticFluxDensity



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity







class LowerCriticalMagneticFluxDensity(MagneticFluxDensity, CondensedMatterPhysicsQuantity):
    """
    Class representing the `LowerCriticalMagneticFluxDensity` entity, which inherits from:
    - MagneticFluxDensity, CondensedMatterPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fd4a6307_f9f7_4b54_b044_caa04e620232'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LowerCriticalMagneticFluxDensity'`
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
    obj = LowerCriticalMagneticFluxDensity(
    
    class_iri='https://w3id.org/emmo#EMMO_fd4a6307_f9f7_4b54_b044_caa04e620232',
    
    class_name='LowerCriticalMagneticFluxDensity',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fd4a6307_f9f7_4b54_b044_caa04e620232',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LowerCriticalMagneticFluxDensity',
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
    

    
    

    

    