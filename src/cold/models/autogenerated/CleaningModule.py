
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparateManufacturingModule import SeparateManufacturing







class Cleaning(SeparateManufacturing):
    """
    Class representing the `Cleaning` entity, which inherits from:
    - SeparateManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_92eaefcb_50be_4237_9ec0_4a019ce24921'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cleaning'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Cleaning(
    
    class_iri='https://w3id.org/emmo#EMMO_92eaefcb_50be_4237_9ec0_4a019ce24921',
    
    class_name='Cleaning',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_92eaefcb_50be_4237_9ec0_4a019ce24921',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cleaning',
        alias="class_name"
    )
    

    
    

    

    