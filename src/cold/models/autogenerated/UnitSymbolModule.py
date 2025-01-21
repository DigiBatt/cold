
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetrologicalSymbolModule import MetrologicalSymbol



from .NonPrefixedUnitModule import NonPrefixedUnit







class UnitSymbol(MetrologicalSymbol, NonPrefixedUnit):
    """
    Class representing the `UnitSymbol` entity, which inherits from:
    - MetrologicalSymbol, NonPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_216f448e_cdbc_4aeb_a529_7a5fe7fc38bb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UnitSymbol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UnitSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_216f448e_cdbc_4aeb_a529_7a5fe7fc38bb',
    
    class_name='UnitSymbol',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_216f448e_cdbc_4aeb_a529_7a5fe7fc38bb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UnitSymbol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    