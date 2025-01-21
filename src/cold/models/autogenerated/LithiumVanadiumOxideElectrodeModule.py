
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VanadiumBasedElectrodeModule import VanadiumBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode







class LithiumVanadiumOxideElectrode(VanadiumBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `LithiumVanadiumOxideElectrode` entity, which inherits from:
    - VanadiumBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b5e91259_cd97_4ed6_9ab2_4b18ef68a35a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumVanadiumOxideElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumVanadiumOxideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b5e91259_cd97_4ed6_9ab2_4b18ef68a35a',
    
    class_name='LithiumVanadiumOxideElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b5e91259_cd97_4ed6_9ab2_4b18ef68a35a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumVanadiumOxideElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    