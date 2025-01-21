
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalObjectModule import PhysicalObject







class Matter(PhysicalObject):
    """
    Class representing the `Matter` entity, which inherits from:
    - PhysicalObject

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5b2222df_4da6_442f_8244_96e9e45887d1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Matter'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Matter(
    
    class_iri='https://w3id.org/emmo#EMMO_5b2222df_4da6_442f_8244_96e9e45887d1',
    
    class_name='Matter',
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5b2222df_4da6_442f_8244_96e9e45887d1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Matter',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    