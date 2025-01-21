
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumericalModule import Numerical



from .MathematicalSymbolModule import MathematicalSymbol



from .SymbolModule import Symbol







class Number(Numerical, MathematicalSymbol, Symbol):
    """
    Class representing the `Number` entity, which inherits from:
    - Numerical, MathematicalSymbol, Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_21f56795_ee72_4858_b571_11cfaa59c1a8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Number'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Number(
    
    class_iri='https://w3id.org/emmo#EMMO_21f56795_ee72_4858_b571_11cfaa59c1a8',
    
    class_name='Number',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_21f56795_ee72_4858_b571_11cfaa59c1a8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Number',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    