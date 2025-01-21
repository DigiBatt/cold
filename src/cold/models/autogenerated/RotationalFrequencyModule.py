
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FrequencyModule import Frequency







class RotationalFrequency(Frequency):
    """
    Class representing the `RotationalFrequency` entity, which inherits from:
    - Frequency

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3789d3c5_77f4_456e_b7ed_40e670f47e52'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RotationalFrequency'`
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
    obj = RotationalFrequency(
    
    class_iri='https://w3id.org/emmo#EMMO_3789d3c5_77f4_456e_b7ed_40e670f47e52',
    
    class_name='RotationalFrequency',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3789d3c5_77f4_456e_b7ed_40e670f47e52',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RotationalFrequency',
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
    

    
    

    

    