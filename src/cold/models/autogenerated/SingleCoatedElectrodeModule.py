
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatedElectrodeModule import CoatedElectrode







class SingleCoatedElectrode(CoatedElectrode):
    """
    Class representing the `SingleCoatedElectrode` entity, which inherits from:
    - CoatedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_418c59bd_dc9d_438b_bc7c_494fbd1bb4f8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SingleCoatedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SingleCoatedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_418c59bd_dc9d_438b_bc7c_494fbd1bb4f8',
    
    class_name='SingleCoatedElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_418c59bd_dc9d_438b_bc7c_494fbd1bb4f8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SingleCoatedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    