
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class TotalNumberOfCycles(PureNumberQuantity, ElectrochemicalQuantity):
    """
    Class representing the `TotalNumberOfCycles` entity, which inherits from:
    - PureNumberQuantity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6d981c04_3ace_4f1b_b0f8_770776cceb6f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TotalNumberOfCycles'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TotalNumberOfCycles(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6d981c04_3ace_4f1b_b0f8_770776cceb6f',
    
    class_name='TotalNumberOfCycles',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6d981c04_3ace_4f1b_b0f8_770776cceb6f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TotalNumberOfCycles',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    