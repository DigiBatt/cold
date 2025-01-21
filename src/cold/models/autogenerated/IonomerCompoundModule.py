
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PolymerCompoundModule import PolymerCompound







class IonomerCompound(PolymerCompound):
    """
    Class representing the `IonomerCompound` entity, which inherits from:
    - PolymerCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_dc68514f_b592_4e1b_a00f_fbb29f2fafbd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IonomerCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IonomerCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_dc68514f_b592_4e1b_a00f_fbb29f2fafbd',
    
    class_name='IonomerCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_dc68514f_b592_4e1b_a00f_fbb29f2fafbd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IonomerCompound',
        alias="class_name"
    )
    

    
    

    

    