
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompressibilityModule import Compressibility



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity







class IsothermalCompressibility(Compressibility, ThermodynamicalQuantity):
    """
    Class representing the `IsothermalCompressibility` entity, which inherits from:
    - Compressibility, ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9bc6da11_528a_44e8_bd9e_c4154eae7e55'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IsothermalCompressibility'`
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
    obj = IsothermalCompressibility(
    
    class_iri='https://w3id.org/emmo#EMMO_9bc6da11_528a_44e8_bd9e_c4154eae7e55',
    
    class_name='IsothermalCompressibility',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9bc6da11_528a_44e8_bd9e_c4154eae7e55',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IsothermalCompressibility',
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
    

    
    

    

    