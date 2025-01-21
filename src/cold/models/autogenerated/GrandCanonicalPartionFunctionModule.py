
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class GrandCanonicalPartionFunction(PhysioChemicalQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `GrandCanonicalPartionFunction` entity, which inherits from:
    - PhysioChemicalQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_80b19ae3_7248_4205_8c79_4e94f5f0444c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GrandCanonicalPartionFunction'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GrandCanonicalPartionFunction(
    
    class_iri='https://w3id.org/emmo#EMMO_80b19ae3_7248_4205_8c79_4e94f5f0444c',
    
    class_name='GrandCanonicalPartionFunction',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_80b19ae3_7248_4205_8c79_4e94f5f0444c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GrandCanonicalPartionFunction',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    