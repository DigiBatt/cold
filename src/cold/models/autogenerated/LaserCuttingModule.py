
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermalCuttingModule import ThermalCutting







class LaserCutting(ThermalCutting):
    """
    Class representing the `LaserCutting` entity, which inherits from:
    - ThermalCutting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c5970406_0b66_4931_8a23_3e81162ba65b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LaserCutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LaserCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_c5970406_0b66_4931_8a23_3e81162ba65b',
    
    class_name='LaserCutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c5970406_0b66_4931_8a23_3e81162ba65b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LaserCutting',
        alias="class_name"
    )
    

    
    

    

    