
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TopQuarkModule import TopQuark



from .GreenQuarkModule import GreenQuark







class GreenTopQuark(TopQuark, GreenQuark):
    """
    Class representing the `GreenTopQuark` entity, which inherits from:
    - TopQuark, GreenQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_76267214_2137_4909_83a4_0b815a62cbc3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenTopQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenTopQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_76267214_2137_4909_83a4_0b815a62cbc3',
    
    class_name='GreenTopQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_76267214_2137_4909_83a4_0b815a62cbc3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenTopQuark',
        alias="class_name"
    )
    

    
    

    

    