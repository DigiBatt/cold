
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SizeDefinedMaterialModule import SizeDefinedMaterial







class NanoMaterial(SizeDefinedMaterial):
    """
    Class representing the `NanoMaterial` entity, which inherits from:
    - SizeDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5d659e25_a508_43ed_903c_3707c7c7cd4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NanoMaterial'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NanoMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_5d659e25_a508_43ed_903c_3707c7c7cd4b',
    
    class_name='NanoMaterial',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5d659e25_a508_43ed_903c_3707c7c7cd4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NanoMaterial',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    