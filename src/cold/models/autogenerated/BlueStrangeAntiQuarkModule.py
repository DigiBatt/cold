
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BlueAntiQuarkModule import BlueAntiQuark



from .StrangeAntiQuarkModule import StrangeAntiQuark







class BlueStrangeAntiQuark(BlueAntiQuark, StrangeAntiQuark):
    """
    Class representing the `BlueStrangeAntiQuark` entity, which inherits from:
    - BlueAntiQuark, StrangeAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_975bdc11_12db_44e7_a3c3_c5436b5e17cc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueStrangeAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueStrangeAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_975bdc11_12db_44e7_a3c3_c5436b5e17cc',
    
    class_name='BlueStrangeAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_975bdc11_12db_44e7_a3c3_c5436b5e17cc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueStrangeAntiQuark',
        alias="class_name"
    )
    

    
    

    

    