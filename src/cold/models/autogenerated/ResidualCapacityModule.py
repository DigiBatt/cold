
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CapacityModule import Capacity







class ResidualCapacity(Capacity):
    """
    Class representing the `ResidualCapacity` entity, which inherits from:
    - Capacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d47985f1_6bd7_4c4f_894f_13a6cab38bb5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ResidualCapacity'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ResidualCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d47985f1_6bd7_4c4f_894f_13a6cab38bb5',
    
    class_name='ResidualCapacity',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d47985f1_6bd7_4c4f_894f_13a6cab38bb5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ResidualCapacity',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    