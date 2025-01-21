
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LiquidSolutionModule import LiquidSolution







class AqueousSolution(LiquidSolution):
    """
    Class representing the `AqueousSolution` entity, which inherits from:
    - LiquidSolution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5cb107ba_7daa_46dd_8f9f_da22a6eac676'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AqueousSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AqueousSolution(
    
    class_iri='https://w3id.org/emmo#EMMO_5cb107ba_7daa_46dd_8f9f_da22a6eac676',
    
    class_name='AqueousSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5cb107ba_7daa_46dd_8f9f_da22a6eac676',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AqueousSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    