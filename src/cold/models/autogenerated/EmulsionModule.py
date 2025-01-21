
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ColloidModule import Colloid



from .LiquidModule import Liquid







class Emulsion(Colloid, Liquid):
    """
    Class representing the `Emulsion` entity, which inherits from:
    - Colloid, Liquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_40e18c93_a1b5_49ff_b06a_d9d932d1fb65'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Emulsion'`
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
    obj = Emulsion(
    
    class_iri='https://w3id.org/emmo#EMMO_40e18c93_a1b5_49ff_b06a_d9d932d1fb65',
    
    class_name='Emulsion',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_40e18c93_a1b5_49ff_b06a_d9d932d1fb65',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Emulsion',
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
    

    
    

    

    