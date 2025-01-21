
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode







class SilverBasedElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `SilverBasedElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f897db90_afd6_42e7_8d1f_0fcba856e45a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SilverBasedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SilverBasedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f897db90_afd6_42e7_8d1f_0fcba856e45a',
    
    class_name='SilverBasedElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f897db90_afd6_42e7_8d1f_0fcba856e45a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SilverBasedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    