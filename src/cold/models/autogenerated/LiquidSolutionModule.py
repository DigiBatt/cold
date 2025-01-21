
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolutionModule import Solution



from .LiquidModule import Liquid







class LiquidSolution(Solution, Liquid):
    """
    Class representing the `LiquidSolution` entity, which inherits from:
    - Solution, Liquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4b3e2374_52a1_4420_8e3f_3ae6b9bf7dff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidSolution(
    
    class_iri='https://w3id.org/emmo#EMMO_4b3e2374_52a1_4420_8e3f_3ae6b9bf7dff',
    
    class_name='LiquidSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4b3e2374_52a1_4420_8e3f_3ae6b9bf7dff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    