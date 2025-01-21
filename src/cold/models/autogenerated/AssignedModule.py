
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EstimatedModule import Estimated







class Assigned(Estimated):
    """
    Class representing the `Assigned` entity, which inherits from:
    - Estimated

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dabe353b_8bfc_4da7_8ac7_8f52786d16f8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Assigned'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Assigned(
    
    class_iri='https://w3id.org/emmo#EMMO_dabe353b_8bfc_4da7_8ac7_8f52786d16f8',
    
    class_name='Assigned',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dabe353b_8bfc_4da7_8ac7_8f52786d16f8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Assigned',
        alias="class_name"
    )
    

    
    

    

    