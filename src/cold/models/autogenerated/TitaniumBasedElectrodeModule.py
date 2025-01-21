
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode







class TitaniumBasedElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `TitaniumBasedElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d90221a0_0da7_4876_9cac_0e943e445f6f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TitaniumBasedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TitaniumBasedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d90221a0_0da7_4876_9cac_0e943e445f6f',
    
    class_name='TitaniumBasedElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d90221a0_0da7_4876_9cac_0e943e445f6f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TitaniumBasedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    