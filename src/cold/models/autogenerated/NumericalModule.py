
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalModule import Mathematical







class Numerical(Mathematical):
    """
    Class representing the `Numerical` entity, which inherits from:
    - Mathematical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4ce76d7f_03f8_45b6_9003_90052a79bfaa'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Numerical'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Numerical(
    
    class_iri='https://w3id.org/emmo#EMMO_4ce76d7f_03f8_45b6_9003_90052a79bfaa',
    
    class_name='Numerical',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4ce76d7f_03f8_45b6_9003_90052a79bfaa',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Numerical',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    