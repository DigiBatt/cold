
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity



from .DiffusionCoefficientModule import DiffusionCoefficient







class DiffusionCoefficientForParticleNumberDensity(AtomicAndNuclearPhysicsQuantity, DiffusionCoefficient):
    """
    Class representing the `DiffusionCoefficientForParticleNumberDensity` entity, which inherits from:
    - AtomicAndNuclearPhysicsQuantity, DiffusionCoefficient

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_56710a21_601b_43bb_88c5_0bd9eca06da2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DiffusionCoefficientForParticleNumberDensity'`
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
    obj = DiffusionCoefficientForParticleNumberDensity(
    
    class_iri='https://w3id.org/emmo#EMMO_56710a21_601b_43bb_88c5_0bd9eca06da2',
    
    class_name='DiffusionCoefficientForParticleNumberDensity',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_56710a21_601b_43bb_88c5_0bd9eca06da2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DiffusionCoefficientForParticleNumberDensity',
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
    

    
    

    

    