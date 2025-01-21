
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IRIModule import IRI







class URI(IRI):
    """
    Class representing the `URI` entity, which inherits from:
    - IRI

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6470bbfa_04a6_4360_9534_1aa18d68329b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'URI'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `figure` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `figure`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = URI(
    
    class_iri='https://w3id.org/emmo#EMMO_6470bbfa_04a6_4360_9534_1aa18d68329b',
    
    class_name='URI',
    
    elucidation="example_value",
    
    figure="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6470bbfa_04a6_4360_9534_1aa18d68329b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'URI',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    figure: Optional[str] = Field(
        None,
        alias="figure"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    