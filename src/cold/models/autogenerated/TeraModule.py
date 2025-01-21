
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMultiplePrefixModule import SIMultiplePrefix







class Tera(SIMultiplePrefix):
    """
    Class representing the `Tera` entity, which inherits from:
    - SIMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_33fe9747_d66f_4f88_b2c1_951279dbca59'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tera'`
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
    obj = Tera(
    
    class_iri='https://w3id.org/emmo#EMMO_33fe9747_d66f_4f88_b2c1_951279dbca59',
    
    class_name='Tera',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_33fe9747_d66f_4f88_b2c1_951279dbca59',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tera',
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
    

    
    

    

    