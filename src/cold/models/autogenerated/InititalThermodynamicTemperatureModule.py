
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicTemperatureModule import ThermodynamicTemperature







class InititalThermodynamicTemperature(ThermodynamicTemperature):
    """
    Class representing the `InititalThermodynamicTemperature` entity, which inherits from:
    - ThermodynamicTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9c9b80a4_a00b_4b91_8e17_3a7831f2bf2f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InititalThermodynamicTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InititalThermodynamicTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9c9b80a4_a00b_4b91_8e17_3a7831f2bf2f',
    
    class_name='InititalThermodynamicTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9c9b80a4_a00b_4b91_8e17_3a7831f2bf2f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InititalThermodynamicTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    