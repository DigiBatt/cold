
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GraphicalModule import Graphical







class Pictorial(Graphical):
    """
    Class representing the `Pictorial` entity, which inherits from:
    - Graphical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1da53c06_9577_4008_8652_272fa3b62be7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Pictorial'`
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
    obj = Pictorial(
    
    class_iri='https://w3id.org/emmo#EMMO_1da53c06_9577_4008_8652_272fa3b62be7',
    
    class_name='Pictorial',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1da53c06_9577_4008_8652_272fa3b62be7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Pictorial',
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
    

    
    

    

    