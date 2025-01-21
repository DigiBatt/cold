
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class Assemblying(JoinManufacturing):
    """
    Class representing the `Assemblying` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_912ac3a2_a124_4233_92dd_06c9aebea46c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Assemblying'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Assemblying(
    
    class_iri='https://w3id.org/emmo#EMMO_912ac3a2_a124_4233_92dd_06c9aebea46c',
    
    class_name='Assemblying',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_912ac3a2_a124_4233_92dd_06c9aebea46c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Assemblying',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    