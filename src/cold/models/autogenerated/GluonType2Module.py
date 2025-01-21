
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType2(Gluon):
    """
    Class representing the `GluonType2` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_70a1c163_7436_4ce3_9784_3aab0e62b900'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType2'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType2(
    
    class_iri='https://w3id.org/emmo#EMMO_70a1c163_7436_4ce3_9784_3aab0e62b900',
    
    class_name='GluonType2',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_70a1c163_7436_4ce3_9784_3aab0e62b900',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType2',
        alias="class_name"
    )
    

    
    

    

    