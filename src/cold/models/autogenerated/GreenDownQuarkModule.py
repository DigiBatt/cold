
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DownQuarkModule import DownQuark



from .GreenQuarkModule import GreenQuark







class GreenDownQuark(DownQuark, GreenQuark):
    """
    Class representing the `GreenDownQuark` entity, which inherits from:
    - DownQuark, GreenQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d5e14e54_fa64_4638_83d3_faced4575e72'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenDownQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenDownQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_d5e14e54_fa64_4638_83d3_faced4575e72',
    
    class_name='GreenDownQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d5e14e54_fa64_4638_83d3_faced4575e72',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenDownQuark',
        alias="class_name"
    )
    

    
    

    

    