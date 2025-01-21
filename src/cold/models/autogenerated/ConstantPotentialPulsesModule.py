
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class ConstantPotentialPulses(ElectricPotentialSignal):
    """
    Class representing the `ConstantPotentialPulses` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_84d37a37_88bd_47db_9425_31f73a81d38c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantPotentialPulses'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantPotentialPulses(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_84d37a37_88bd_47db_9425_31f73a81d38c',
    
    class_name='ConstantPotentialPulses',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_84d37a37_88bd_47db_9425_31f73a81d38c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantPotentialPulses',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    