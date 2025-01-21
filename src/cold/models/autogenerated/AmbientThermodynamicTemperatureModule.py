
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicTemperatureModule import ThermodynamicTemperature







class AmbientThermodynamicTemperature(ThermodynamicTemperature):
    """
    Class representing the `AmbientThermodynamicTemperature` entity, which inherits from:
    - ThermodynamicTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_39a44af0_0e1a_4859_b550_bdabad64386e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmbientThermodynamicTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmbientThermodynamicTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_39a44af0_0e1a_4859_b550_bdabad64386e',
    
    class_name='AmbientThermodynamicTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_39a44af0_0e1a_4859_b550_bdabad64386e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmbientThermodynamicTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    