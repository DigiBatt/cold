
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoredEnergyModule import StoredEnergy







class TotalEnergy(StoredEnergy):
    """
    Class representing the `TotalEnergy` entity, which inherits from:
    - StoredEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f986d97_445f_4075_a5ce_ddde598a47a9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TotalEnergy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TotalEnergy(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f986d97_445f_4075_a5ce_ddde598a47a9',
    
    class_name='TotalEnergy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f986d97_445f_4075_a5ce_ddde598a47a9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TotalEnergy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    