
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity







class ChargingConstantCurrentPercentage(RatioQuantity):
    """
    Class representing the `ChargingConstantCurrentPercentage` entity, which inherits from:
    - RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7f073272_8925_4344_995c_a5a6dd1fcde6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingConstantCurrentPercentage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingConstantCurrentPercentage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7f073272_8925_4344_995c_a5a6dd1fcde6',
    
    class_name='ChargingConstantCurrentPercentage',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7f073272_8925_4344_995c_a5a6dd1fcde6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingConstantCurrentPercentage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    