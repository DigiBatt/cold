
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity







class Diffusivity(ISQDerivedQuantity):
    """
    Class representing the `Diffusivity` entity, which inherits from:
    - ISQDerivedQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_37b24a94_cae0_4d7a_9519_9f7692dec607'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Diffusivity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Diffusivity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_37b24a94_cae0_4d7a_9519_9f7692dec607',
    
    class_name='Diffusivity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_37b24a94_cae0_4d7a_9519_9f7692dec607',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Diffusivity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    