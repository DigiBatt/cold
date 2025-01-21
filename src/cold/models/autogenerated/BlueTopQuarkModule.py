
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TopQuarkModule import TopQuark



from .BlueQuarkModule import BlueQuark







class BlueTopQuark(TopQuark, BlueQuark):
    """
    Class representing the `BlueTopQuark` entity, which inherits from:
    - TopQuark, BlueQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3ab4154b_d163_4236_8251_8917b07c2788'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueTopQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueTopQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_3ab4154b_d163_4236_8251_8917b07c2788',
    
    class_name='BlueTopQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3ab4154b_d163_4236_8251_8917b07c2788',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueTopQuark',
        alias="class_name"
    )
    

    
    

    

    