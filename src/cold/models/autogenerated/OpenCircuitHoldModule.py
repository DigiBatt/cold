
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PotentiometryModule import Potentiometry







class OpenCircuitHold(Potentiometry):
    """
    Class representing the `OpenCircuitHold` entity, which inherits from:
    - Potentiometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#OpenCircuitHold'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OpenCircuitHold'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OpenCircuitHold(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#OpenCircuitHold',
    
    class_name='OpenCircuitHold',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#OpenCircuitHold',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OpenCircuitHold',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    