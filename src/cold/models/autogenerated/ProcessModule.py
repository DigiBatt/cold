
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PersistenceModule import Persistence







class Process(Persistence):
    """
    Class representing the `Process` entity, which inherits from:
    - Persistence

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_43e9a05d_98af_41b4_92f6_00f79a09bfce'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Process'`
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
    obj = Process(
    
    class_iri='https://w3id.org/emmo#EMMO_43e9a05d_98af_41b4_92f6_00f79a09bfce',
    
    class_name='Process',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_43e9a05d_98af_41b4_92f6_00f79a09bfce',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Process',
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
    

    
    

    

    