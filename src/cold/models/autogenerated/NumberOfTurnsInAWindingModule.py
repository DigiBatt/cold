
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectromagneticQuantityModule import ElectromagneticQuantity



from .PureNumberQuantityModule import PureNumberQuantity







class NumberOfTurnsInAWinding(ElectromagneticQuantity, PureNumberQuantity):
    """
    Class representing the `NumberOfTurnsInAWinding` entity, which inherits from:
    - ElectromagneticQuantity, PureNumberQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eefaa0ef_e7d4_4633_bf79_655bb55f4a49'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfTurnsInAWinding'`
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
    obj = NumberOfTurnsInAWinding(
    
    class_iri='https://w3id.org/emmo#EMMO_eefaa0ef_e7d4_4633_bf79_655bb55f4a49',
    
    class_name='NumberOfTurnsInAWinding',
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eefaa0ef_e7d4_4633_bf79_655bb55f4a49',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfTurnsInAWinding',
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
    

    
    

    

    