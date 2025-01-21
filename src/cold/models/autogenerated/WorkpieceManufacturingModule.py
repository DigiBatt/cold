
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturingModule import Manufacturing







class WorkpieceManufacturing(Manufacturing):
    """
    Class representing the `WorkpieceManufacturing` entity, which inherits from:
    - Manufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8786cb47_8e1f_4968_9b15_f6d41fc51252'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WorkpieceManufacturing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WorkpieceManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_8786cb47_8e1f_4968_9b15_f6d41fc51252',
    
    class_name='WorkpieceManufacturing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8786cb47_8e1f_4968_9b15_f6d41fc51252',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WorkpieceManufacturing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    