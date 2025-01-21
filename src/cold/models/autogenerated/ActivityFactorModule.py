
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class ActivityFactor(PhysioChemicalQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `ActivityFactor` entity, which inherits from:
    - PhysioChemicalQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_254ff869_7d28_42dd_aedc_adb4cc8ad0cb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivityFactor'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActivityFactor(
    
    class_iri='https://w3id.org/emmo#EMMO_254ff869_7d28_42dd_aedc_adb4cc8ad0cb',
    
    class_name='ActivityFactor',
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_254ff869_7d28_42dd_aedc_adb4cc8ad0cb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivityFactor',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    