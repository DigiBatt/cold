
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SISubMultiplePrefixModule import SISubMultiplePrefix







class Micro(SISubMultiplePrefix):
    """
    Class representing the `Micro` entity, which inherits from:
    - SISubMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6da1b965_768c_4cf0_8873_44f2035133ba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Micro'`
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
    obj = Micro(
    
    class_iri='https://w3id.org/emmo#EMMO_6da1b965_768c_4cf0_8873_44f2035133ba',
    
    class_name='Micro',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6da1b965_768c_4cf0_8873_44f2035133ba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Micro',
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
    

    
    

    

    