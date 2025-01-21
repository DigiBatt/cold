
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class StaircasePotentialRamp(ElectricPotentialSignal):
    """
    Class representing the `StaircasePotentialRamp` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d359386f_ae2d_4ad4_9616_464e2111b67d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StaircasePotentialRamp'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StaircasePotentialRamp(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d359386f_ae2d_4ad4_9616_464e2111b67d',
    
    class_name='StaircasePotentialRamp',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d359386f_ae2d_4ad4_9616_464e2111b67d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StaircasePotentialRamp',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    