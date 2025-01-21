
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UpQuarkModule import UpQuark



from .BlueQuarkModule import BlueQuark







class BlueUpQuark(UpQuark, BlueQuark):
    """
    Class representing the `BlueUpQuark` entity, which inherits from:
    - UpQuark, BlueQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f321cf62_99e4_418e_bb3e_3dfcc91f701f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueUpQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueUpQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_f321cf62_99e4_418e_bb3e_3dfcc91f701f',
    
    class_name='BlueUpQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f321cf62_99e4_418e_bb3e_3dfcc91f701f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueUpQuark',
        alias="class_name"
    )
    

    
    

    

    