
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FrequencyModule import Frequency



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class LowerFrequencyLimit(Frequency, ElectrochemicalControlQuantity):
    """
    Class representing the `LowerFrequencyLimit` entity, which inherits from:
    - Frequency, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b66d6553_6136_4754_902a_707e414210c2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LowerFrequencyLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LowerFrequencyLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b66d6553_6136_4754_902a_707e414210c2',
    
    class_name='LowerFrequencyLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b66d6553_6136_4754_902a_707e414210c2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LowerFrequencyLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    