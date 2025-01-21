
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BottomAntiQuarkModule import BottomAntiQuark



from .BlueAntiQuarkModule import BlueAntiQuark







class BlueBottomAntiQuark(BottomAntiQuark, BlueAntiQuark):
    """
    Class representing the `BlueBottomAntiQuark` entity, which inherits from:
    - BottomAntiQuark, BlueAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_29d24a97_f3bd_4e9b_934d_9da589f719e5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueBottomAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueBottomAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_29d24a97_f3bd_4e9b_934d_9da589f719e5',
    
    class_name='BlueBottomAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_29d24a97_f3bd_4e9b_934d_9da589f719e5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueBottomAntiQuark',
        alias="class_name"
    )
    

    
    

    

    