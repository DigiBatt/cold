
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity



from .ReciprocalLengthModule import ReciprocalLength







class AngularReciprocalLatticeVector(CondensedMatterPhysicsQuantity, ReciprocalLength):
    """
    Class representing the `AngularReciprocalLatticeVector` entity, which inherits from:
    - CondensedMatterPhysicsQuantity, ReciprocalLength

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7254c8be_965d_4b3c_b3be_12c5578bee7c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AngularReciprocalLatticeVector'`
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
    obj = AngularReciprocalLatticeVector(
    
    class_iri='https://w3id.org/emmo#EMMO_7254c8be_965d_4b3c_b3be_12c5578bee7c',
    
    class_name='AngularReciprocalLatticeVector',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7254c8be_965d_4b3c_b3be_12c5578bee7c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AngularReciprocalLatticeVector',
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
    

    
    

    

    