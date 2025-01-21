
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity



from .AngleModule import Angle







class BraggAngle(CondensedMatterPhysicsQuantity, Angle):
    """
    Class representing the `BraggAngle` entity, which inherits from:
    - CondensedMatterPhysicsQuantity, Angle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_034bc7dd_a8c2_4ed0_8b51_66ac9b00342f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BraggAngle'`
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
    obj = BraggAngle(
    
    class_iri='https://w3id.org/emmo#EMMO_034bc7dd_a8c2_4ed0_8b51_66ac9b00342f',
    
    class_name='BraggAngle',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_034bc7dd_a8c2_4ed0_8b51_66ac9b00342f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BraggAngle',
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
    

    
    

    

    