
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ForceModule import Force



from .MechanicalQuantityModule import MechanicalQuantity







class RollingResistance(Force, MechanicalQuantity):
    """
    Class representing the `RollingResistance` entity, which inherits from:
    - Force, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0ab4306c_ba36_4a6e_941e_474ed04e8ccf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RollingResistance'`
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
    obj = RollingResistance(
    
    class_iri='https://w3id.org/emmo#EMMO_0ab4306c_ba36_4a6e_941e_474ed04e8ccf',
    
    class_name='RollingResistance',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0ab4306c_ba36_4a6e_941e_474ed04e8ccf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RollingResistance',
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
    

    
    

    

    