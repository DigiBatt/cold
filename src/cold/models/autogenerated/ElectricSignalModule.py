
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SignalModule import Signal







class ElectricSignal(Signal):
    """
    Class representing the `ElectricSignal` entity, which inherits from:
    - Signal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_898971cb_a9fc_4955_8abf_5d7163a9fe6c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricSignal'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricSignal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_898971cb_a9fc_4955_8abf_5d7163a9fe6c',
    
    class_name='ElectricSignal',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_898971cb_a9fc_4955_8abf_5d7163a9fe6c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricSignal',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    