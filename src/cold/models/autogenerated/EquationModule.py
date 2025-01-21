
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalFormulaModule import MathematicalFormula



from .CausalSystemModule import CausalSystem



from .MathematicalModule import Mathematical







class Equation(MathematicalFormula, CausalSystem, Mathematical):
    """
    Class representing the `Equation` entity, which inherits from:
    - MathematicalFormula, CausalSystem, Mathematical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e56ee3eb_7609_4ae1_8bed_51974f0960a6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Equation'`
        - **Alias**: `class_name`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Equation(
    
    class_iri='https://w3id.org/emmo#EMMO_e56ee3eb_7609_4ae1_8bed_51974f0960a6',
    
    class_name='Equation',
    
    hasSpatialPart="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e56ee3eb_7609_4ae1_8bed_51974f0960a6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Equation',
        alias="class_name"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    