
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class NPRatio(RatioQuantity, ElectrochemicalQuantity):
    """
    Class representing the `NPRatio` entity, which inherits from:
    - RatioQuantity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_05012606_b93d_4016_bbc7_8a927efdf723'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NPRatio'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NPRatio(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_05012606_b93d_4016_bbc7_8a927efdf723',
    
    class_name='NPRatio',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_05012606_b93d_4016_bbc7_8a927efdf723',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NPRatio',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    