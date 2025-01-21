
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OpticalTestingModule import OpticalTesting







class DynamicLightScattering(OpticalTesting):
    """
    Class representing the `DynamicLightScattering` entity, which inherits from:
    - OpticalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DynamicLightScattering'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DynamicLightScattering'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DynamicLightScattering(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DynamicLightScattering',
    
    class_name='DynamicLightScattering',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DynamicLightScattering',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DynamicLightScattering',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    