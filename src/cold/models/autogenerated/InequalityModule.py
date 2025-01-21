
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalFormulaModule import MathematicalFormula







class Inequality(MathematicalFormula):
    """
    Class representing the `Inequality` entity, which inherits from:
    - MathematicalFormula

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0b6ebe5a_0026_4bef_a1c1_5be00df9f98e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Inequality'`
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
    obj = Inequality(
    
    class_iri='https://w3id.org/emmo#EMMO_0b6ebe5a_0026_4bef_a1c1_5be00df9f98e',
    
    class_name='Inequality',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0b6ebe5a_0026_4bef_a1c1_5be00df9f98e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Inequality',
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
    

    
    

    

    