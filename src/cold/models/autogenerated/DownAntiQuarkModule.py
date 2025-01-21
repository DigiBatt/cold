
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .DownAntiQuarkTypeModule import DownAntiQuarkType







class DownAntiQuark(FirstGenerationFermion, DownAntiQuarkType):
    """
    Class representing the `DownAntiQuark` entity, which inherits from:
    - FirstGenerationFermion, DownAntiQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e7adbaa9_ae34_42e4_8101_cbd38851dcab'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DownAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DownAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_e7adbaa9_ae34_42e4_8101_cbd38851dcab',
    
    class_name='DownAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e7adbaa9_ae34_42e4_8101_cbd38851dcab',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DownAntiQuark',
        alias="class_name"
    )
    

    
    

    

    