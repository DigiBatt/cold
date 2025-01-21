
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkpieceManufacturingModule import WorkpieceManufacturing







class MergingManufacturing(WorkpieceManufacturing):
    """
    Class representing the `MergingManufacturing` entity, which inherits from:
    - WorkpieceManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb85216f_b872_4ee5_9f62_655aa2ae0470'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MergingManufacturing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MergingManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_eb85216f_b872_4ee5_9f62_655aa2ae0470',
    
    class_name='MergingManufacturing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb85216f_b872_4ee5_9f62_655aa2ae0470',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MergingManufacturing',
        alias="class_name"
    )
    

    
    

    

    