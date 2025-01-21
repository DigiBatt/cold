
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TitaniumBasedElectrodeModule import TitaniumBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode







class SodiumTitaniumPhosphateElectrode(TitaniumBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `SodiumTitaniumPhosphateElectrode` entity, which inherits from:
    - TitaniumBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cff80dd5_19a9_4357_8fb9_410a978153e2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumTitaniumPhosphateElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumTitaniumPhosphateElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cff80dd5_19a9_4357_8fb9_410a978153e2',
    
    class_name='SodiumTitaniumPhosphateElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cff80dd5_19a9_4357_8fb9_410a978153e2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumTitaniumPhosphateElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    