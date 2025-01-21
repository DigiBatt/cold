
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AmountConcentrationModule import AmountConcentration



from .LimitQuantityModule import LimitQuantity







class ConcentrationLimit(AmountConcentration, LimitQuantity):
    """
    Class representing the `ConcentrationLimit` entity, which inherits from:
    - AmountConcentration, LimitQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5eae657f_5914_4252_85c6_3fc772dea113'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConcentrationLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConcentrationLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5eae657f_5914_4252_85c6_3fc772dea113',
    
    class_name='ConcentrationLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5eae657f_5914_4252_85c6_3fc772dea113',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConcentrationLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    