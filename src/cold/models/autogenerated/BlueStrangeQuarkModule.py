
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrangeQuarkModule import StrangeQuark



from .BlueQuarkModule import BlueQuark







class BlueStrangeQuark(StrangeQuark, BlueQuark):
    """
    Class representing the `BlueStrangeQuark` entity, which inherits from:
    - StrangeQuark, BlueQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b8fa18b7_14c7_42cd_bd5f_4fc073677a5b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueStrangeQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueStrangeQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_b8fa18b7_14c7_42cd_bd5f_4fc073677a5b',
    
    class_name='BlueStrangeQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b8fa18b7_14c7_42cd_bd5f_4fc073677a5b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueStrangeQuark',
        alias="class_name"
    )
    

    
    

    

    