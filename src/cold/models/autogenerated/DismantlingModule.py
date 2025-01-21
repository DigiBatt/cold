
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparateManufacturingModule import SeparateManufacturing







class Dismantling(SeparateManufacturing):
    """
    Class representing the `Dismantling` entity, which inherits from:
    - SeparateManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c7171429_b9e3_4812_95c1_e97309370538'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Dismantling'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Dismantling(
    
    class_iri='https://w3id.org/emmo#EMMO_c7171429_b9e3_4812_95c1_e97309370538',
    
    class_name='Dismantling',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c7171429_b9e3_4812_95c1_e97309370538',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Dismantling',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    