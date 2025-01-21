
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellCurrentModule import CellCurrent



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class CurrentScanRate(CellCurrent, ElectrochemicalControlQuantity):
    """
    Class representing the `CurrentScanRate` entity, which inherits from:
    - CellCurrent, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f046d602_22ea_4f9b_9101_319f510d39f0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentScanRate'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentScanRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f046d602_22ea_4f9b_9101_319f510d39f0',
    
    class_name='CurrentScanRate',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f046d602_22ea_4f9b_9101_319f510d39f0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentScanRate',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    