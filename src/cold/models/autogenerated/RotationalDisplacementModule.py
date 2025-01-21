
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpaceAndTimeQuantityModule import SpaceAndTimeQuantity



from .AngleModule import Angle







class RotationalDisplacement(SpaceAndTimeQuantity, Angle):
    """
    Class representing the `RotationalDisplacement` entity, which inherits from:
    - SpaceAndTimeQuantity, Angle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dfd22e00_993b_40cc_a4ad_1134c1e3007a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RotationalDisplacement'`
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
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RotationalDisplacement(
    
    class_iri='https://w3id.org/emmo#EMMO_dfd22e00_993b_40cc_a4ad_1134c1e3007a',
    
    class_name='RotationalDisplacement',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dfd22e00_993b_40cc_a4ad_1134c1e3007a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RotationalDisplacement',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    