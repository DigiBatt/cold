
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DownQuarkModule import DownQuark



from .BlueQuarkModule import BlueQuark







class BlueDownQuark(DownQuark, BlueQuark):
    """
    Class representing the `BlueDownQuark` entity, which inherits from:
    - DownQuark, BlueQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_94b07779_910a_4e56_bb34_2754dae4e376'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueDownQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueDownQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_94b07779_910a_4e56_bb34_2754dae4e376',
    
    class_name='BlueDownQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_94b07779_910a_4e56_bb34_2754dae4e376',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueDownQuark',
        alias="class_name"
    )
    

    
    

    

    