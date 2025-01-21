
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity







class MaximumEfficiency(ISQDimensionlessQuantity, ThermodynamicalQuantity):
    """
    Class representing the `MaximumEfficiency` entity, which inherits from:
    - ISQDimensionlessQuantity, ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_476cb776_8219_418d_92e8_2fe04b1fe5cf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumEfficiency'`
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
    obj = MaximumEfficiency(
    
    class_iri='https://w3id.org/emmo#EMMO_476cb776_8219_418d_92e8_2fe04b1fe5cf',
    
    class_name='MaximumEfficiency',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_476cb776_8219_418d_92e8_2fe04b1fe5cf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumEfficiency',
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
    

    
    

    

    