
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThirdGenerationFermionModule import ThirdGenerationFermion



from .UpAntiQuarkTypeModule import UpAntiQuarkType







class TopAntiQuark(ThirdGenerationFermion, UpAntiQuarkType):
    """
    Class representing the `TopAntiQuark` entity, which inherits from:
    - ThirdGenerationFermion, UpAntiQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b14894ce_aad8_45e6_8035_f902c0d339ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TopAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TopAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_b14894ce_aad8_45e6_8035_f902c0d339ad',
    
    class_name='TopAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b14894ce_aad8_45e6_8035_f902c0d339ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TopAntiQuark',
        alias="class_name"
    )
    

    
    

    

    