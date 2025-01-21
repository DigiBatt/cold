
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TitaniumBasedElectrodeModule import TitaniumBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode







class SodiumTitaniumOxideElectrode(TitaniumBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `SodiumTitaniumOxideElectrode` entity, which inherits from:
    - TitaniumBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5f51531_1452_4654_82e5_0505491c2c7d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumTitaniumOxideElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumTitaniumOxideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5f51531_1452_4654_82e5_0505491c2c7d',
    
    class_name='SodiumTitaniumOxideElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5f51531_1452_4654_82e5_0505491c2c7d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumTitaniumOxideElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    