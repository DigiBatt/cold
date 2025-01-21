
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpaceAndTimeQuantityModule import SpaceAndTimeQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class Rotation(SpaceAndTimeQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `Rotation` entity, which inherits from:
    - SpaceAndTimeQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_16d72037_3243_4018_ac6c_0015f661d3c3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Rotation'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Rotation(
    
    class_iri='https://w3id.org/emmo#EMMO_16d72037_3243_4018_ac6c_0015f661d3c3',
    
    class_name='Rotation',
    
    wikidataReference="example_value",
    
    IEVReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_16d72037_3243_4018_ac6c_0015f661d3c3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Rotation',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    