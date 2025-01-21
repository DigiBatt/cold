
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMultiplePrefixModule import SIMultiplePrefix







class Mega(SIMultiplePrefix):
    """
    Class representing the `Mega` entity, which inherits from:
    - SIMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_85ee9154_5a3e_482e_aa37_c617ff1947ff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Mega'`
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
    obj = Mega(
    
    class_iri='https://w3id.org/emmo#EMMO_85ee9154_5a3e_482e_aa37_c617ff1947ff',
    
    class_name='Mega',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_85ee9154_5a3e_482e_aa37_c617ff1947ff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Mega',
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
    

    
    

    

    