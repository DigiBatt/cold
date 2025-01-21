
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MechanicalQuantityModule import MechanicalQuantity



from .RatioQuantityModule import RatioQuantity







class MechanicalEfficiency(MechanicalQuantity, RatioQuantity):
    """
    Class representing the `MechanicalEfficiency` entity, which inherits from:
    - MechanicalQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7f9b4abe_0bf1_48dc_9bd0_ea34e926ec85'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MechanicalEfficiency'`
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
    obj = MechanicalEfficiency(
    
    class_iri='https://w3id.org/emmo#EMMO_7f9b4abe_0bf1_48dc_9bd0_ea34e926ec85',
    
    class_name='MechanicalEfficiency',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7f9b4abe_0bf1_48dc_9bd0_ea34e926ec85',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MechanicalEfficiency',
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
    

    
    

    

    