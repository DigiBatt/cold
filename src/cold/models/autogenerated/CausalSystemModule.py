
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalStructureModule import CausalStructure







class CausalSystem(CausalStructure):
    """
    Class representing the `CausalSystem` entity, which inherits from:
    - CausalStructure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e7aac247_31d6_4b2e_9fd2_e842b1b7ccac'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausalSystem'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausalSystem(
    
    class_iri='https://w3id.org/emmo#EMMO_e7aac247_31d6_4b2e_9fd2_e842b1b7ccac',
    
    class_name='CausalSystem',
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e7aac247_31d6_4b2e_9fd2_e842b1b7ccac',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausalSystem',
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
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    