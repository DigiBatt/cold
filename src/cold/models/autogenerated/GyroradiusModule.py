
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RadiusModule import Radius



from .AtomicAndNuclearPhysicsQuantityModule import AtomicAndNuclearPhysicsQuantity







class Gyroradius(Radius, AtomicAndNuclearPhysicsQuantity):
    """
    Class representing the `Gyroradius` entity, which inherits from:
    - Radius, AtomicAndNuclearPhysicsQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aa078194_12df_4b10_b264_6595d2472570'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gyroradius'`
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
    obj = Gyroradius(
    
    class_iri='https://w3id.org/emmo#EMMO_aa078194_12df_4b10_b264_6595d2472570',
    
    class_name='Gyroradius',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aa078194_12df_4b10_b264_6595d2472570',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gyroradius',
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
    

    
    

    

    