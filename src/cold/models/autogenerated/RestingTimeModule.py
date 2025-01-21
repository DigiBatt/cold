
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DurationModule import Duration



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class RestingTime(Duration, ElectrochemicalControlQuantity):
    """
    Class representing the `RestingTime` entity, which inherits from:
    - Duration, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2678a656_4a27_4706_8dde_b0a93e9b92fa'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RestingTime'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RestingTime(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2678a656_4a27_4706_8dde_b0a93e9b92fa',
    
    class_name='RestingTime',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2678a656_4a27_4706_8dde_b0a93e9b92fa',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RestingTime',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    