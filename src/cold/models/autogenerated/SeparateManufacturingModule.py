
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkpieceManufacturingModule import WorkpieceManufacturing







class SeparateManufacturing(WorkpieceManufacturing):
    """
    Class representing the `SeparateManufacturing` entity, which inherits from:
    - WorkpieceManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_90589553_5625_4074_8f0d_0532fd7eb42b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SeparateManufacturing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SeparateManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_90589553_5625_4074_8f0d_0532fd7eb42b',
    
    class_name='SeparateManufacturing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_90589553_5625_4074_8f0d_0532fd7eb42b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SeparateManufacturing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    