
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DurationModule import Duration



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class PulseDuration(Duration, ElectrochemicalControlQuantity):
    """
    Class representing the `PulseDuration` entity, which inherits from:
    - Duration, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3cd0e74e_292c_48ed_a831_4cb8753d9a56'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulseDuration'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PulseDuration(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3cd0e74e_292c_48ed_a831_4cb8753d9a56',
    
    class_name='PulseDuration',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3cd0e74e_292c_48ed_a831_4cb8753d9a56',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulseDuration',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    