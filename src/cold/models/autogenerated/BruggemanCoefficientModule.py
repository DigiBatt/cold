
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity







class BruggemanCoefficient(PureNumberQuantity):
    """
    Class representing the `BruggemanCoefficient` entity, which inherits from:
    - PureNumberQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5c34b3b5_c9c4_477d_809a_3f682f995aa9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BruggemanCoefficient'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BruggemanCoefficient(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5c34b3b5_c9c4_477d_809a_3f682f995aa9',
    
    class_name='BruggemanCoefficient',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5c34b3b5_c9c4_477d_809a_3f682f995aa9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BruggemanCoefficient',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    