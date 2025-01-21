
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .ElectrochemicalKineticQuantityModule import ElectrochemicalKineticQuantity







class ReactionRateConstant(ISQDerivedQuantity, ElectrochemicalKineticQuantity):
    """
    Class representing the `ReactionRateConstant` entity, which inherits from:
    - ISQDerivedQuantity, ElectrochemicalKineticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0335e3f6_d1d8_4daa_8376_a9285f1bc9f1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReactionRateConstant'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReactionRateConstant(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0335e3f6_d1d8_4daa_8376_a9285f1bc9f1',
    
    class_name='ReactionRateConstant',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0335e3f6_d1d8_4daa_8376_a9285f1bc9f1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReactionRateConstant',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    