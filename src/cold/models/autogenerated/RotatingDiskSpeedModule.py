
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RotationalFrequencyModule import RotationalFrequency



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class RotatingDiskSpeed(RotationalFrequency, ElectrochemicalControlQuantity):
    """
    Class representing the `RotatingDiskSpeed` entity, which inherits from:
    - RotationalFrequency, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1900143f_cbc0_415f_9057_9382022a7bfe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RotatingDiskSpeed'`
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
    obj = RotatingDiskSpeed(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1900143f_cbc0_415f_9057_9382022a7bfe',
    
    class_name='RotatingDiskSpeed',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1900143f_cbc0_415f_9057_9382022a7bfe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RotatingDiskSpeed',
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
    

    
    

    

    