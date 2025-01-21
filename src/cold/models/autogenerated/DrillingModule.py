
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MachiningModule import Machining







class Drilling(Machining):
    """
    Class representing the `Drilling` entity, which inherits from:
    - Machining

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c1dad83e_974f_432e_ac92_d016f2445279'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Drilling'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Drilling(
    
    class_iri='https://w3id.org/emmo#EMMO_c1dad83e_974f_432e_ac92_d016f2445279',
    
    class_name='Drilling',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c1dad83e_974f_432e_ac92_d016f2445279',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Drilling',
        alias="class_name"
    )
    

    
    

    

    