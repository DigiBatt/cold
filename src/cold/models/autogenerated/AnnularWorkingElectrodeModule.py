
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkingElectrodeModule import WorkingElectrode







class AnnularWorkingElectrode(WorkingElectrode):
    """
    Class representing the `AnnularWorkingElectrode` entity, which inherits from:
    - WorkingElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3a77b5e7_9646_4154_bf8f_5f798989e5f3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnnularWorkingElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AnnularWorkingElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3a77b5e7_9646_4154_bf8f_5f798989e5f3',
    
    class_name='AnnularWorkingElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3a77b5e7_9646_4154_bf8f_5f798989e5f3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnnularWorkingElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    