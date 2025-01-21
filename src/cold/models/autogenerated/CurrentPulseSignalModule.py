
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentSignalModule import ElectricCurrentSignal







class CurrentPulseSignal(ElectricCurrentSignal):
    """
    Class representing the `CurrentPulseSignal` entity, which inherits from:
    - ElectricCurrentSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_712c791a_d593_4732_af73_493f7bc50999'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentPulseSignal'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentPulseSignal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_712c791a_d593_4732_af73_493f7bc50999',
    
    class_name='CurrentPulseSignal',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_712c791a_d593_4732_af73_493f7bc50999',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentPulseSignal',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    