
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManganesePhosphateBasedElectrodeModule import ManganesePhosphateBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode







class LithiumManganesePhosphateElectrode(ManganesePhosphateBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `LithiumManganesePhosphateElectrode` entity, which inherits from:
    - ManganesePhosphateBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_713200a1_952b_49e2_90b7_deba229f6bbe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumManganesePhosphateElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumManganesePhosphateElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_713200a1_952b_49e2_90b7_deba229f6bbe',
    
    class_name='LithiumManganesePhosphateElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_713200a1_952b_49e2_90b7_deba229f6bbe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumManganesePhosphateElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    