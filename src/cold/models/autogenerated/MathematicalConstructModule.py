
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalModule import Mathematical



from .SymbolicConstructModule import SymbolicConstruct







class MathematicalConstruct(Mathematical, SymbolicConstruct):
    """
    Class representing the `MathematicalConstruct` entity, which inherits from:
    - Mathematical, SymbolicConstruct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ffe760a2_9d1f_4aef_8bee_1f450f9cb00d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MathematicalConstruct'`
        - **Alias**: `class_name`
    
    - `hasProperPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasProperPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MathematicalConstruct(
    
    class_iri='https://w3id.org/emmo#EMMO_ffe760a2_9d1f_4aef_8bee_1f450f9cb00d',
    
    class_name='MathematicalConstruct',
    
    hasProperPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ffe760a2_9d1f_4aef_8bee_1f450f9cb00d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MathematicalConstruct',
        alias="class_name"
    )
    
    hasProperPart: Optional[str] = Field(
        None,
        alias="hasProperPart"
    )
    

    
    

    

    