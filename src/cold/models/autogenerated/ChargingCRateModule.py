
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CRateModule import CRate







class ChargingCRate(CRate):
    """
    Class representing the `ChargingCRate` entity, which inherits from:
    - CRate

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a7dc73e2_d4aa_4dfc_8b4d_cb611f1501fb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingCRate'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingCRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a7dc73e2_d4aa_4dfc_8b4d_cb611f1501fb',
    
    class_name='ChargingCRate',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a7dc73e2_d4aa_4dfc_8b4d_cb611f1501fb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingCRate',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    