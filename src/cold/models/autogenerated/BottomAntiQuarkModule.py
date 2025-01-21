
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThirdGenerationFermionModule import ThirdGenerationFermion



from .DownAntiQuarkTypeModule import DownAntiQuarkType







class BottomAntiQuark(ThirdGenerationFermion, DownAntiQuarkType):
    """
    Class representing the `BottomAntiQuark` entity, which inherits from:
    - ThirdGenerationFermion, DownAntiQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_12a3441c_4fe8_4d9c_a7db_9e86ce6c41ee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BottomAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BottomAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_12a3441c_4fe8_4d9c_a7db_9e86ce6c41ee',
    
    class_name='BottomAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_12a3441c_4fe8_4d9c_a7db_9e86ce6c41ee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BottomAntiQuark',
        alias="class_name"
    )
    

    
    

    

    