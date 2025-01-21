
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MachiningModule import Machining







class Planing(Machining):
    """
    Class representing the `Planing` entity, which inherits from:
    - Machining

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f5655090_2266_41cb_b2e9_3b4569c45731'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Planing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Planing(
    
    class_iri='https://w3id.org/emmo#EMMO_f5655090_2266_41cb_b2e9_3b4569c45731',
    
    class_name='Planing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f5655090_2266_41cb_b2e9_3b4569c45731',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Planing',
        alias="class_name"
    )
    

    
    

    

    