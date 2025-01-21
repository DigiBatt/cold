
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManganesePhosphateBasedElectrodeModule import ManganesePhosphateBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode







class LithiumManganeseIronPhosphateElectrode(ManganesePhosphateBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `LithiumManganeseIronPhosphateElectrode` entity, which inherits from:
    - ManganesePhosphateBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9109b3f6_112b_456d_ae45_b82c271c656b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumManganeseIronPhosphateElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumManganeseIronPhosphateElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9109b3f6_112b_456d_ae45_b82c271c656b',
    
    class_name='LithiumManganeseIronPhosphateElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9109b3f6_112b_456d_ae45_b82c271c656b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumManganeseIronPhosphateElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    