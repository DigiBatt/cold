
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class DifferentialCapacity(ElectrochemicalQuantity):
    """
    Class representing the `DifferentialCapacity` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10104499_6580_4867_9c5d_b9882c89c2f7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DifferentialCapacity'`
        - **Alias**: `class_name`
    
    - `newareLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `newareLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DifferentialCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10104499_6580_4867_9c5d_b9882c89c2f7',
    
    class_name='DifferentialCapacity',
    
    newareLabel="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10104499_6580_4867_9c5d_b9882c89c2f7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DifferentialCapacity',
        alias="class_name"
    )
    
    newareLabel: Optional[str] = Field(
        None,
        alias="newareLabel"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    