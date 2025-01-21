
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode







class GoldBasedElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `GoldBasedElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52547692_f773_4e3f_8c8b_1d9d39bc3c8c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GoldBasedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GoldBasedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52547692_f773_4e3f_8c8b_1d9d39bc3c8c',
    
    class_name='GoldBasedElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52547692_f773_4e3f_8c8b_1d9d39bc3c8c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GoldBasedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    