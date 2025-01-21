
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalConstructModule import MathematicalConstruct



from .MathematicalModule import Mathematical



from .SymbolicConstructModule import SymbolicConstruct







class MathematicalFormula(MathematicalConstruct, Mathematical, SymbolicConstruct):
    """
    Class representing the `MathematicalFormula` entity, which inherits from:
    - MathematicalConstruct, Mathematical, SymbolicConstruct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_88470739_03d3_4c47_a03e_b30a1288d50c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MathematicalFormula'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MathematicalFormula(
    
    class_iri='https://w3id.org/emmo#EMMO_88470739_03d3_4c47_a03e_b30a1288d50c',
    
    class_name='MathematicalFormula',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_88470739_03d3_4c47_a03e_b30a1288d50c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MathematicalFormula',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    