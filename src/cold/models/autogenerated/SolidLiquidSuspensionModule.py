
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SuspensionModule import Suspension



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class SolidLiquidSuspension(Suspension, SolidMixture, Solid):
    """
    Class representing the `SolidLiquidSuspension` entity, which inherits from:
    - Suspension, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_33e0ac8b_a318_4285_b1de_e95347784632'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidLiquidSuspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidLiquidSuspension(
    
    class_iri='https://w3id.org/emmo#EMMO_33e0ac8b_a318_4285_b1de_e95347784632',
    
    class_name='SolidLiquidSuspension',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_33e0ac8b_a318_4285_b1de_e95347784632',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidLiquidSuspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    