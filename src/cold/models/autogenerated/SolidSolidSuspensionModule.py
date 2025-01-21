
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SuspensionModule import Suspension



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class SolidSolidSuspension(Suspension, SolidMixture, Solid):
    """
    Class representing the `SolidSolidSuspension` entity, which inherits from:
    - Suspension, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2dd512a1_5187_47cc_b0b8_141214e22b59'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidSolidSuspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidSolidSuspension(
    
    class_iri='https://w3id.org/emmo#EMMO_2dd512a1_5187_47cc_b0b8_141214e22b59',
    
    class_name='SolidSolidSuspension',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2dd512a1_5187_47cc_b0b8_141214e22b59',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidSolidSuspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    