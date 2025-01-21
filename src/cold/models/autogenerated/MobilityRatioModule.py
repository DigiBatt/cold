
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity



from .RatioQuantityModule import RatioQuantity







class MobilityRatio(CondensedMatterPhysicsQuantity, RatioQuantity):
    """
    Class representing the `MobilityRatio` entity, which inherits from:
    - CondensedMatterPhysicsQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b0a1578_ae70_4cd1_940d_54d9c220d8f7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MobilityRatio'`
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
    obj = MobilityRatio(
    
    class_iri='https://w3id.org/emmo#EMMO_2b0a1578_ae70_4cd1_940d_54d9c220d8f7',
    
    class_name='MobilityRatio',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b0a1578_ae70_4cd1_940d_54d9c220d8f7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MobilityRatio',
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
    

    
    

    

    