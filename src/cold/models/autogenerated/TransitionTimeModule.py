
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class TransitionTime(ElectrochemicalQuantity):
    """
    Class representing the `TransitionTime` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae9882de_d6a2_4525_a84f_80947c10f1cb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransitionTime'`
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
    obj = TransitionTime(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae9882de_d6a2_4525_a84f_80947c10f1cb',
    
    class_name='TransitionTime',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae9882de_d6a2_4525_a84f_80947c10f1cb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransitionTime',
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
    

    
    

    

    