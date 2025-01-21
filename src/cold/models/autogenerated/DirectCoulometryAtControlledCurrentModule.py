
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoulometryModule import Coulometry







class DirectCoulometryAtControlledCurrent(Coulometry):
    """
    Class representing the `DirectCoulometryAtControlledCurrent` entity, which inherits from:
    - Coulometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DirectCoulometryAtControlledCurrent'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DirectCoulometryAtControlledCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DirectCoulometryAtControlledCurrent(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DirectCoulometryAtControlledCurrent',
    
    class_name='DirectCoulometryAtControlledCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DirectCoulometryAtControlledCurrent',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DirectCoulometryAtControlledCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    