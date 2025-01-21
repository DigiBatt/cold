
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CRateModule import CRate



from .RatioQuantityModule import RatioQuantity







class DischargingCRate(CRate, RatioQuantity):
    """
    Class representing the `DischargingCRate` entity, which inherits from:
    - CRate, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_25e20915_c35d_4bee_ad31_736235a79780'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DischargingCRate'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DischargingCRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_25e20915_c35d_4bee_ad31_736235a79780',
    
    class_name='DischargingCRate',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_25e20915_c35d_4bee_ad31_736235a79780',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DischargingCRate',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    