
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class PRate(RatioQuantity, ElectrochemicalQuantity):
    """
    Class representing the `PRate` entity, which inherits from:
    - RatioQuantity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c4120ce7_f1ff_4917_b59e_002454a65040'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PRate'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c4120ce7_f1ff_4917_b59e_002454a65040',
    
    class_name='PRate',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c4120ce7_f1ff_4917_b59e_002454a65040',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PRate',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    