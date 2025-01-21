
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalSystemModule import CausalSystem







class CausalConvexSystem(CausalSystem):
    """
    Class representing the `CausalConvexSystem` entity, which inherits from:
    - CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a6d8e2e2_5e61_4838_977b_9a5dea421fc1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausalConvexSystem'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausalConvexSystem(
    
    class_iri='https://w3id.org/emmo#EMMO_a6d8e2e2_5e61_4838_977b_9a5dea421fc1',
    
    class_name='CausalConvexSystem',
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a6d8e2e2_5e61_4838_977b_9a5dea421fc1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausalConvexSystem',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    