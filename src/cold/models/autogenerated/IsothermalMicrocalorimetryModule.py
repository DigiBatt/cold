
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermochemicalTestingModule import ThermochemicalTesting







class IsothermalMicrocalorimetry(ThermochemicalTesting):
    """
    Class representing the `IsothermalMicrocalorimetry` entity, which inherits from:
    - ThermochemicalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#IsothermalMicrocalorimetry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IsothermalMicrocalorimetry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IsothermalMicrocalorimetry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#IsothermalMicrocalorimetry',
    
    class_name='IsothermalMicrocalorimetry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#IsothermalMicrocalorimetry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IsothermalMicrocalorimetry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    