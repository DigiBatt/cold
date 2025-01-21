
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .UpAntiQuarkTypeModule import UpAntiQuarkType







class UpAntiQuark(FirstGenerationFermion, UpAntiQuarkType):
    """
    Class representing the `UpAntiQuark` entity, which inherits from:
    - FirstGenerationFermion, UpAntiQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5293c41e_4bbf_4aaa_8479_efd0737a0e8d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UpAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UpAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_5293c41e_4bbf_4aaa_8479_efd0737a0e8d',
    
    class_name='UpAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5293c41e_4bbf_4aaa_8479_efd0737a0e8d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UpAntiQuark',
        alias="class_name"
    )
    

    
    

    

    