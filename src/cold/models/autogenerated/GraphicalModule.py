
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VisualModule import Visual







class Graphical(Visual):
    """
    Class representing the `Graphical` entity, which inherits from:
    - Visual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c74da218_9147_4f03_92d1_8894abca55f3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Graphical'`
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
    obj = Graphical(
    
    class_iri='https://w3id.org/emmo#EMMO_c74da218_9147_4f03_92d1_8894abca55f3',
    
    class_name='Graphical',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c74da218_9147_4f03_92d1_8894abca55f3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Graphical',
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
    

    
    

    

    