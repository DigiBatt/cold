
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MechanicalTestingModule import MechanicalTesting







class HardnessTesting(MechanicalTesting):
    """
    Class representing the `HardnessTesting` entity, which inherits from:
    - MechanicalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#HardnessTesting'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardnessTesting'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardnessTesting(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#HardnessTesting',
    
    class_name='HardnessTesting',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#HardnessTesting',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardnessTesting',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    