
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CRateModule import CRate







class FinishingCRate(CRate):
    """
    Class representing the `FinishingCRate` entity, which inherits from:
    - CRate

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50674621_09ae_4f03_8ee9_3997b88c8b2a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FinishingCRate'`
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
    obj = FinishingCRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50674621_09ae_4f03_8ee9_3997b88c8b2a',
    
    class_name='FinishingCRate',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50674621_09ae_4f03_8ee9_3997b88c8b2a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FinishingCRate',
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
    

    
    

    

    