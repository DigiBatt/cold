
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SISubMultiplePrefixModule import SISubMultiplePrefix







class Nano(SISubMultiplePrefix):
    """
    Class representing the `Nano` entity, which inherits from:
    - SISubMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_afb29c1a_eba4_4ba7_b6a1_62e9023c94ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Nano'`
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
    obj = Nano(
    
    class_iri='https://w3id.org/emmo#EMMO_afb29c1a_eba4_4ba7_b6a1_62e9023c94ec',
    
    class_name='Nano',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_afb29c1a_eba4_4ba7_b6a1_62e9023c94ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Nano',
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
    

    
    

    

    