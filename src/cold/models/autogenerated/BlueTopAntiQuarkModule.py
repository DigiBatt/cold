
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TopAntiQuarkModule import TopAntiQuark



from .BlueAntiQuarkModule import BlueAntiQuark







class BlueTopAntiQuark(TopAntiQuark, BlueAntiQuark):
    """
    Class representing the `BlueTopAntiQuark` entity, which inherits from:
    - TopAntiQuark, BlueAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ad6b0980_fa04_4ec3_b033_6aed9f4ed17c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueTopAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueTopAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_ad6b0980_fa04_4ec3_b033_6aed9f4ed17c',
    
    class_name='BlueTopAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ad6b0980_fa04_4ec3_b033_6aed9f4ed17c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueTopAntiQuark',
        alias="class_name"
    )
    

    
    

    

    