
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode







class NickelBasedElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `NickelBasedElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d2aaaf4_1a8a_4a32_abd8_7d0fdf0ae9d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NickelBasedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NickelBasedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d2aaaf4_1a8a_4a32_abd8_7d0fdf0ae9d2',
    
    class_name='NickelBasedElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d2aaaf4_1a8a_4a32_abd8_7d0fdf0ae9d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NickelBasedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    