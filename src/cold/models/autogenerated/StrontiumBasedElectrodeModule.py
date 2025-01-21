
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode







class StrontiumBasedElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `StrontiumBasedElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46ac0fd3_2b8e_40aa_bf5d_19cf1dd39052'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumBasedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumBasedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46ac0fd3_2b8e_40aa_bf5d_19cf1dd39052',
    
    class_name='StrontiumBasedElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46ac0fd3_2b8e_40aa_bf5d_19cf1dd39052',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumBasedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    