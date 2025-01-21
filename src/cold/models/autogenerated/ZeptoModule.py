
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SISubMultiplePrefixModule import SISubMultiplePrefix







class Zepto(SISubMultiplePrefix):
    """
    Class representing the `Zepto` entity, which inherits from:
    - SISubMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4db5c662_b065_49e4_96eb_826699fa8048'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Zepto'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `hasNumericalValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNumericalValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Zepto(
    
    class_iri='https://w3id.org/emmo#EMMO_4db5c662_b065_49e4_96eb_826699fa8048',
    
    class_name='Zepto',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4db5c662_b065_49e4_96eb_826699fa8048',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Zepto',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    
    hasNumericalValue: Optional[str] = Field(
        None,
        alias="hasNumericalValue"
    )
    

    
    

    

    