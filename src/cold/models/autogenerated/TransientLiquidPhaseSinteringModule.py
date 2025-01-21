
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class TransientLiquidPhaseSintering(Sintering):
    """
    Class representing the `TransientLiquidPhaseSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e9907887_f266_4d81_9b2d_ba5137c914dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransientLiquidPhaseSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransientLiquidPhaseSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_e9907887_f266_4d81_9b2d_ba5137c914dd',
    
    class_name='TransientLiquidPhaseSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e9907887_f266_4d81_9b2d_ba5137c914dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransientLiquidPhaseSintering',
        alias="class_name"
    )
    

    
    

    

    