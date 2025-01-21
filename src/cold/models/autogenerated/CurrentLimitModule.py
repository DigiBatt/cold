
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .LimitQuantityModule import LimitQuantity







class CurrentLimit(ElectricCurrent, LimitQuantity):
    """
    Class representing the `CurrentLimit` entity, which inherits from:
    - ElectricCurrent, LimitQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74de2c33_84fc_4c2f_afe1_56d169149114'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74de2c33_84fc_4c2f_afe1_56d169149114',
    
    class_name='CurrentLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74de2c33_84fc_4c2f_afe1_56d169149114',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    