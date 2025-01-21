
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AblationModule import Ablation







class ThermalCutting(Ablation):
    """
    Class representing the `ThermalCutting` entity, which inherits from:
    - Ablation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c9f0abb6_d3e8_459e_bacc_c14ed5481998'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermalCutting'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermalCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_c9f0abb6_d3e8_459e_bacc_c14ed5481998',
    
    class_name='ThermalCutting',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c9f0abb6_d3e8_459e_bacc_c14ed5481998',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermalCutting',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    