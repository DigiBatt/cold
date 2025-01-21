
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpaceAndTimeQuantityModule import SpaceAndTimeQuantity



from .AngleModule import Angle







class PhaseAngle(SpaceAndTimeQuantity, Angle):
    """
    Class representing the `PhaseAngle` entity, which inherits from:
    - SpaceAndTimeQuantity, Angle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2a0e5777_348c_475b_adf0_1b1e71a29bc9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhaseAngle'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhaseAngle(
    
    class_iri='https://w3id.org/emmo#EMMO_2a0e5777_348c_475b_adf0_1b1e71a29bc9',
    
    class_name='PhaseAngle',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2a0e5777_348c_475b_adf0_1b1e71a29bc9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhaseAngle',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    