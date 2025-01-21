
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PulseDurationModule import PulseDuration







class MaximumDischargingPulseDuration(PulseDuration):
    """
    Class representing the `MaximumDischargingPulseDuration` entity, which inherits from:
    - PulseDuration

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5dc0c1d_0926_4268_89f0_4519a326eabc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumDischargingPulseDuration'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumDischargingPulseDuration(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5dc0c1d_0926_4268_89f0_4519a326eabc',
    
    class_name='MaximumDischargingPulseDuration',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5dc0c1d_0926_4268_89f0_4519a326eabc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumDischargingPulseDuration',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    