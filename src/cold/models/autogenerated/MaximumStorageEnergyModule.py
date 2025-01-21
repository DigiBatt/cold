
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatedEnergyModule import RatedEnergy







class MaximumStorageEnergy(RatedEnergy):
    """
    Class representing the `MaximumStorageEnergy` entity, which inherits from:
    - RatedEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1cdeedbf_7f9a_4e1f_a297_204a6e16b718'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumStorageEnergy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumStorageEnergy(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1cdeedbf_7f9a_4e1f_a297_204a6e16b718',
    
    class_name='MaximumStorageEnergy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1cdeedbf_7f9a_4e1f_a297_204a6e16b718',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumStorageEnergy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    