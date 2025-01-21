
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondGenerationFermionModule import SecondGenerationFermion



from .UpAntiQuarkTypeModule import UpAntiQuarkType







class CharmAntiQuark(SecondGenerationFermion, UpAntiQuarkType):
    """
    Class representing the `CharmAntiQuark` entity, which inherits from:
    - SecondGenerationFermion, UpAntiQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_68c0e0cd_6afd_4eb7_9dfa_91c2462002c9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharmAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharmAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_68c0e0cd_6afd_4eb7_9dfa_91c2462002c9',
    
    class_name='CharmAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_68c0e0cd_6afd_4eb7_9dfa_91c2462002c9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharmAntiQuark',
        alias="class_name"
    )
    

    
    

    

    