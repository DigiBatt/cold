
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatingManufacturingModule import CoatingManufacturing







class PowderCoating(CoatingManufacturing):
    """
    Class representing the `PowderCoating` entity, which inherits from:
    - CoatingManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_658b8bca_203a_49a6_920b_96b5baf5e199'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PowderCoating'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PowderCoating(
    
    class_iri='https://w3id.org/emmo#EMMO_658b8bca_203a_49a6_920b_96b5baf5e199',
    
    class_name='PowderCoating',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_658b8bca_203a_49a6_920b_96b5baf5e199',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PowderCoating',
        alias="class_name"
    )
    

    
    

    

    