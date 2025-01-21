
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class IncreasingPotentialPulses(ElectricPotentialSignal):
    """
    Class representing the `IncreasingPotentialPulses` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_77be01ef_49bd_4f2e_bec8_eec0894b8562'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IncreasingPotentialPulses'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IncreasingPotentialPulses(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_77be01ef_49bd_4f2e_bec8_eec0894b8562',
    
    class_name='IncreasingPotentialPulses',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_77be01ef_49bd_4f2e_bec8_eec0894b8562',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IncreasingPotentialPulses',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    