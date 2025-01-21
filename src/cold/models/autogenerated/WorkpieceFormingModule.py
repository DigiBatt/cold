
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturingModule import Manufacturing







class WorkpieceForming(Manufacturing):
    """
    Class representing the `WorkpieceForming` entity, which inherits from:
    - Manufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dd4b7d81_28a9_4801_8831_4cbab217e362'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WorkpieceForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WorkpieceForming(
    
    class_iri='https://w3id.org/emmo#EMMO_dd4b7d81_28a9_4801_8831_4cbab217e362',
    
    class_name='WorkpieceForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dd4b7d81_28a9_4801_8831_4cbab217e362',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WorkpieceForming',
        alias="class_name"
    )
    

    
    

    

    