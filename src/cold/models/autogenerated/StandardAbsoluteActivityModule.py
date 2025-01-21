
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AbsoluteActivityModule import AbsoluteActivity



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity







class StandardAbsoluteActivity(AbsoluteActivity, PhysioChemicalQuantity):
    """
    Class representing the `StandardAbsoluteActivity` entity, which inherits from:
    - AbsoluteActivity, PhysioChemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d368744e_bb2e_4d40_a7ef_762505b6027e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardAbsoluteActivity'`
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
    obj = StandardAbsoluteActivity(
    
    class_iri='https://w3id.org/emmo#EMMO_d368744e_bb2e_4d40_a7ef_762505b6027e',
    
    class_name='StandardAbsoluteActivity',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d368744e_bb2e_4d40_a7ef_762505b6027e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardAbsoluteActivity',
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
    

    
    

    

    