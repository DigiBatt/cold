
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .LatentHeatModule import LatentHeat







class LatentHeatOfPhaseTransition(PhysioChemicalQuantity, LatentHeat):
    """
    Class representing the `LatentHeatOfPhaseTransition` entity, which inherits from:
    - PhysioChemicalQuantity, LatentHeat

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6bae1f5a_1644_4da3_b3e4_0a01171034ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LatentHeatOfPhaseTransition'`
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
    obj = LatentHeatOfPhaseTransition(
    
    class_iri='https://w3id.org/emmo#EMMO_6bae1f5a_1644_4da3_b3e4_0a01171034ad',
    
    class_name='LatentHeatOfPhaseTransition',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6bae1f5a_1644_4da3_b3e4_0a01171034ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LatentHeatOfPhaseTransition',
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
    

    
    

    

    