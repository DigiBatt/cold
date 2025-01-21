
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiElectronTypeModule import AntiElectronType



from .ThirdGenerationFermionModule import ThirdGenerationFermion







class AntiTau(AntiElectronType, ThirdGenerationFermion):
    """
    Class representing the `AntiTau` entity, which inherits from:
    - AntiElectronType, ThirdGenerationFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b4abf29e_aab7_4c2f_af0b_536a92ef327f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiTau'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AntiTau(
    
    class_iri='https://w3id.org/emmo#EMMO_b4abf29e_aab7_4c2f_af0b_536a92ef327f',
    
    class_name='AntiTau',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b4abf29e_aab7_4c2f_af0b_536a92ef327f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiTau',
        alias="class_name"
    )
    

    
    

    

    