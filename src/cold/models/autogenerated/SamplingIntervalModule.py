
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DurationModule import Duration



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class SamplingInterval(Duration, ElectrochemicalControlQuantity):
    """
    Class representing the `SamplingInterval` entity, which inherits from:
    - Duration, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52ac73c7_763c_4fda_93cd_a2db9dfc2dab'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SamplingInterval'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SamplingInterval(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52ac73c7_763c_4fda_93cd_a2db9dfc2dab',
    
    class_name='SamplingInterval',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_52ac73c7_763c_4fda_93cd_a2db9dfc2dab',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SamplingInterval',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    