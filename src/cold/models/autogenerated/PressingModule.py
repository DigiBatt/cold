
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class Pressing(JoinManufacturing):
    """
    Class representing the `Pressing` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bbf12904_e25e_4f49_87f3_8bd210a6b535'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Pressing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Pressing(
    
    class_iri='https://w3id.org/emmo#EMMO_bbf12904_e25e_4f49_87f3_8bd210a6b535',
    
    class_name='Pressing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bbf12904_e25e_4f49_87f3_8bd210a6b535',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Pressing',
        alias="class_name"
    )
    

    
    

    

    