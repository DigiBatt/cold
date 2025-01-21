
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class PermanentLiquidPhaseSintering(Sintering):
    """
    Class representing the `PermanentLiquidPhaseSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1acb552d_281a_40a4_9d55_5e31b85d4dc1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PermanentLiquidPhaseSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PermanentLiquidPhaseSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_1acb552d_281a_40a4_9d55_5e31b85d4dc1',
    
    class_name='PermanentLiquidPhaseSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1acb552d_281a_40a4_9d55_5e31b85d4dc1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PermanentLiquidPhaseSintering',
        alias="class_name"
    )
    

    
    

    

    