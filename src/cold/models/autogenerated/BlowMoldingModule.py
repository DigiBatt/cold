
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPlasticModule import FormingFromPlastic







class BlowMolding(FormingFromPlastic):
    """
    Class representing the `BlowMolding` entity, which inherits from:
    - FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_381b6a6e_6e8e_461a_8591_d7a60e823d4d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlowMolding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlowMolding(
    
    class_iri='https://w3id.org/emmo#EMMO_381b6a6e_6e8e_461a_8591_d7a60e823d4d',
    
    class_name='BlowMolding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_381b6a6e_6e8e_461a_8591_d7a60e823d4d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlowMolding',
        alias="class_name"
    )
    

    
    

    

    