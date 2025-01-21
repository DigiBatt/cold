
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SISubMultiplePrefixModule import SISubMultiplePrefix







class Atto(SISubMultiplePrefix):
    """
    Class representing the `Atto` entity, which inherits from:
    - SISubMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e9722f13_947c_444e_82ef_1ce045f6637c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Atto'`
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
    obj = Atto(
    
    class_iri='https://w3id.org/emmo#EMMO_e9722f13_947c_444e_82ef_1ce045f6637c',
    
    class_name='Atto',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e9722f13_947c_444e_82ef_1ce045f6637c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Atto',
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
    

    
    

    

    