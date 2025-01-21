
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiQuarkModule import AntiQuark







class GreenAntiQuark(AntiQuark):
    """
    Class representing the `GreenAntiQuark` entity, which inherits from:
    - AntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ffd65547_6a7e_499d_826a_cee9e7d669fd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_ffd65547_6a7e_499d_826a_cee9e7d669fd',
    
    class_name='GreenAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ffd65547_6a7e_499d_826a_cee9e7d669fd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenAntiQuark',
        alias="class_name"
    )
    

    
    

    

    