
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BottomQuarkModule import BottomQuark



from .BlueQuarkModule import BlueQuark







class BlueBottomQuark(BottomQuark, BlueQuark):
    """
    Class representing the `BlueBottomQuark` entity, which inherits from:
    - BottomQuark, BlueQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e1ae2427_e902_44ae_bac2_8ac80939c457'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueBottomQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueBottomQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_e1ae2427_e902_44ae_bac2_8ac80939c457',
    
    class_name='BlueBottomQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e1ae2427_e902_44ae_bac2_8ac80939c457',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueBottomQuark',
        alias="class_name"
    )
    

    
    

    

    