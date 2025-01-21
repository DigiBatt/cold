
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LeptonModule import Lepton







class ElectronType(Lepton):
    """
    Class representing the `ElectronType` entity, which inherits from:
    - Lepton

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d2fc9fc2_7f50_495d_a311_1832349db6cb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronType'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectronType(
    
    class_iri='https://w3id.org/emmo#EMMO_d2fc9fc2_7f50_495d_a311_1832349db6cb',
    
    class_name='ElectronType',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d2fc9fc2_7f50_495d_a311_1832349db6cb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronType',
        alias="class_name"
    )
    

    
    

    

    