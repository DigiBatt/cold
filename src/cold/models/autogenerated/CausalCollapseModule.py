
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalInteractionModule import FundamentalInteraction







class CausalCollapse(FundamentalInteraction):
    """
    Class representing the `CausalCollapse` entity, which inherits from:
    - FundamentalInteraction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1f2bfb9f_ecc6_46a0_9e41_2d6fcbf59e4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausalCollapse'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausalCollapse(
    
    class_iri='https://w3id.org/emmo#EMMO_1f2bfb9f_ecc6_46a0_9e41_2d6fcbf59e4b',
    
    class_name='CausalCollapse',
    
    conceptualisation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1f2bfb9f_ecc6_46a0_9e41_2d6fcbf59e4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausalCollapse',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    

    
    

    

    