
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetalOxideElectrodeModule import MetalOxideElectrode







class RutheniumOxideElectrode(MetalOxideElectrode):
    """
    Class representing the `RutheniumOxideElectrode` entity, which inherits from:
    - MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10a91aba_da41_4309_a926_ddc0f285c2c1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RutheniumOxideElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RutheniumOxideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10a91aba_da41_4309_a926_ddc0f285c2c1',
    
    class_name='RutheniumOxideElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10a91aba_da41_4309_a926_ddc0f285c2c1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RutheniumOxideElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    