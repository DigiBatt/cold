
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiLeptonModule import AntiLepton







class AntiElectronType(AntiLepton):
    """
    Class representing the `AntiElectronType` entity, which inherits from:
    - AntiLepton

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4e36a0b8_e6c7_456e_bef5_c830e3c0ed17'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiElectronType'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AntiElectronType(
    
    class_iri='https://w3id.org/emmo#EMMO_4e36a0b8_e6c7_456e_bef5_c830e3c0ed17',
    
    class_name='AntiElectronType',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4e36a0b8_e6c7_456e_bef5_c830e3c0ed17',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiElectronType',
        alias="class_name"
    )
    

    
    

    

    