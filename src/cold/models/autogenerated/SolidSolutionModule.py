
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolutionModule import Solution



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class SolidSolution(Solution, SolidMixture, Solid):
    """
    Class representing the `SolidSolution` entity, which inherits from:
    - Solution, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5e77f00d_5c0a_44e7_baf1_2c2a4cb5b3ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidSolution(
    
    class_iri='https://w3id.org/emmo#EMMO_5e77f00d_5c0a_44e7_baf1_2c2a4cb5b3ae',
    
    class_name='SolidSolution',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5e77f00d_5c0a_44e7_baf1_2c2a4cb5b3ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    