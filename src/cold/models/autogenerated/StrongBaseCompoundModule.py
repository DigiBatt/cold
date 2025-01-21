
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BaseModule import Base







class StrongBaseCompound(Base):
    """
    Class representing the `StrongBaseCompound` entity, which inherits from:
    - Base

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_bed1a22c_8b61_467a_86a0_d24c7b910653'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrongBaseCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrongBaseCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_bed1a22c_8b61_467a_86a0_d24c7b910653',
    
    class_name='StrongBaseCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_bed1a22c_8b61_467a_86a0_d24c7b910653',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrongBaseCompound',
        alias="class_name"
    )
    

    
    

    

    