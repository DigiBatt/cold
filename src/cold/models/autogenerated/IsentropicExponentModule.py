
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity







class IsentropicExponent(ISQDimensionlessQuantity, ThermodynamicalQuantity):
    """
    Class representing the `IsentropicExponent` entity, which inherits from:
    - ISQDimensionlessQuantity, ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8040a6f6_4736_4dd2_8d1c_f2c13cb77a71'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IsentropicExponent'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IsentropicExponent(
    
    class_iri='https://w3id.org/emmo#EMMO_8040a6f6_4736_4dd2_8d1c_f2c13cb77a71',
    
    class_name='IsentropicExponent',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8040a6f6_4736_4dd2_8d1c_f2c13cb77a71',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IsentropicExponent',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    