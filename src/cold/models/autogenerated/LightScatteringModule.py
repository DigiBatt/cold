
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OpticalTestingModule import OpticalTesting







class LightScattering(OpticalTesting):
    """
    Class representing the `LightScattering` entity, which inherits from:
    - OpticalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#LightScattering'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LightScattering'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LightScattering(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#LightScattering',
    
    class_name='LightScattering',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#LightScattering',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LightScattering',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    