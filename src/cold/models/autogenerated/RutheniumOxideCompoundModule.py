
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class RutheniumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `RutheniumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4ca80d73_ea14_4a81_9df1_8a16ecbfd041'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RutheniumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RutheniumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4ca80d73_ea14_4a81_9df1_8a16ecbfd041',
    
    class_name='RutheniumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4ca80d73_ea14_4a81_9df1_8a16ecbfd041',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RutheniumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    