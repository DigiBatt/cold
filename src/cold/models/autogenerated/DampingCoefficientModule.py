
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FrequencyModule import Frequency







class DampingCoefficient(Frequency):
    """
    Class representing the `DampingCoefficient` entity, which inherits from:
    - Frequency

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ab3e812f_4d0f_4290_83fb_b2f5963f3772'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DampingCoefficient'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DampingCoefficient(
    
    class_iri='https://w3id.org/emmo#EMMO_ab3e812f_4d0f_4290_83fb_b2f5963f3772',
    
    class_name='DampingCoefficient',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ab3e812f_4d0f_4290_83fb_b2f5963f3772',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DampingCoefficient',
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
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    