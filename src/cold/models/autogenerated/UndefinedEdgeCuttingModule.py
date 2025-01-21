
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparateManufacturingModule import SeparateManufacturing







class UndefinedEdgeCutting(SeparateManufacturing):
    """
    Class representing the `UndefinedEdgeCutting` entity, which inherits from:
    - SeparateManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_24788d59_32f5_4339_a42a_43a102ec14a8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UndefinedEdgeCutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UndefinedEdgeCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_24788d59_32f5_4339_a42a_43a102ec14a8',
    
    class_name='UndefinedEdgeCutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_24788d59_32f5_4339_a42a_43a102ec14a8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UndefinedEdgeCutting',
        alias="class_name"
    )
    

    
    

    

    