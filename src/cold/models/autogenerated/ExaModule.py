
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMultiplePrefixModule import SIMultiplePrefix







class Exa(SIMultiplePrefix):
    """
    Class representing the `Exa` entity, which inherits from:
    - SIMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3f2d29d9_6d27_43bd_a1bc_85475eae98be'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Exa'`
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
    obj = Exa(
    
    class_iri='https://w3id.org/emmo#EMMO_3f2d29d9_6d27_43bd_a1bc_85475eae98be',
    
    class_name='Exa',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3f2d29d9_6d27_43bd_a1bc_85475eae98be',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Exa',
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
    

    
    

    

    