
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class LimitQuantity(ElectrochemicalControlQuantity):
    """
    Class representing the `LimitQuantity` entity, which inherits from:
    - ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b395a244_3a75_4737_be38_981bfa1277fe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LimitQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LimitQuantity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b395a244_3a75_4737_be38_981bfa1277fe',
    
    class_name='LimitQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b395a244_3a75_4737_be38_981bfa1277fe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LimitQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    