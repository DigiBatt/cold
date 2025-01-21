
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PowerModule import Power







class RadiantFlux(Power):
    """
    Class representing the `RadiantFlux` entity, which inherits from:
    - Power

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e46f3f24_c2ec_4552_8dd4_cfc5c0a89c09'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RadiantFlux'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RadiantFlux(
    
    class_iri='https://w3id.org/emmo#EMMO_e46f3f24_c2ec_4552_8dd4_cfc5c0a89c09',
    
    class_name='RadiantFlux',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e46f3f24_c2ec_4552_8dd4_cfc5c0a89c09',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RadiantFlux',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    