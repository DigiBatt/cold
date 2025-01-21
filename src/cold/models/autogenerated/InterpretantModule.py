
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SignModule import Sign







class Interpretant(Sign):
    """
    Class representing the `Interpretant` entity, which inherits from:
    - Sign

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_054af807_85cd_4a13_8eba_119dfdaaf38b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Interpretant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Interpretant(
    
    class_iri='https://w3id.org/emmo#EMMO_054af807_85cd_4a13_8eba_119dfdaaf38b',
    
    class_name='Interpretant',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_054af807_85cd_4a13_8eba_119dfdaaf38b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Interpretant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    