
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaximumTemperatureModule import MaximumTemperature







class MaximumDischargingTemperature(MaximumTemperature):
    """
    Class representing the `MaximumDischargingTemperature` entity, which inherits from:
    - MaximumTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_de612af2_a029_4a02_8090_4a75ab13271d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumDischargingTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumDischargingTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_de612af2_a029_4a02_8090_4a75ab13271d',
    
    class_name='MaximumDischargingTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_de612af2_a029_4a02_8090_4a75ab13271d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumDischargingTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    