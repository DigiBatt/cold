
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalConstructModule import MathematicalConstruct



from .MathematicalModule import Mathematical



from .SymbolicConstructModule import SymbolicConstruct







class Expression(MathematicalConstruct, Mathematical, SymbolicConstruct):
    """
    Class representing the `Expression` entity, which inherits from:
    - MathematicalConstruct, Mathematical, SymbolicConstruct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f9bc8b52_85e9_4b53_b969_dd7724d5b8e4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Expression'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Expression(
    
    class_iri='https://w3id.org/emmo#EMMO_f9bc8b52_85e9_4b53_b969_dd7724d5b8e4',
    
    class_name='Expression',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f9bc8b52_85e9_4b53_b969_dd7724d5b8e4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Expression',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    