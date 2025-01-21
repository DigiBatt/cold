
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMultiplePrefixModule import SIMultiplePrefix







class Deca(SIMultiplePrefix):
    """
    Class representing the `Deca` entity, which inherits from:
    - SIMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e07a252a_6913_49d6_9038_37a258b2d95e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Deca'`
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
    obj = Deca(
    
    class_iri='https://w3id.org/emmo#EMMO_e07a252a_6913_49d6_9038_37a258b2d95e',
    
    class_name='Deca',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e07a252a_6913_49d6_9038_37a258b2d95e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Deca',
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
    

    
    

    

    