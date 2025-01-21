
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TitaniumBasedElectrodeModule import TitaniumBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode







class SodiumMetatitanateElectrode(TitaniumBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `SodiumMetatitanateElectrode` entity, which inherits from:
    - TitaniumBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_103c9e6c_9c26_430a_9fb9_f4f041e970b0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumMetatitanateElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumMetatitanateElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_103c9e6c_9c26_430a_9fb9_f4f041e970b0',
    
    class_name='SodiumMetatitanateElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_103c9e6c_9c26_430a_9fb9_f4f041e970b0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumMetatitanateElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    