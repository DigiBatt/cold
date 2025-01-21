
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BaseModule import Base







class WeakBaseCompound(Base):
    """
    Class representing the `WeakBaseCompound` entity, which inherits from:
    - Base

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_8e5448fc_1916_4afb_9fd9_2489797f6922'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WeakBaseCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WeakBaseCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_8e5448fc_1916_4afb_9fd9_2489797f6922',
    
    class_name='WeakBaseCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_8e5448fc_1916_4afb_9fd9_2489797f6922',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WeakBaseCompound',
        alias="class_name"
    )
    

    
    

    

    