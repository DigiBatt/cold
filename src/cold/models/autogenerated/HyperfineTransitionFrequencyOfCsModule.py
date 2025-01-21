
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FrequencyModule import Frequency



from .SIExactConstantModule import SIExactConstant







class HyperfineTransitionFrequencyOfCs(Frequency, SIExactConstant):
    """
    Class representing the `HyperfineTransitionFrequencyOfCs` entity, which inherits from:
    - Frequency, SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f96feb3f_4438_4e43_aa44_7458c4d87fc2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HyperfineTransitionFrequencyOfCs'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HyperfineTransitionFrequencyOfCs(
    
    class_iri='https://w3id.org/emmo#EMMO_f96feb3f_4438_4e43_aa44_7458c4d87fc2',
    
    class_name='HyperfineTransitionFrequencyOfCs',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f96feb3f_4438_4e43_aa44_7458c4d87fc2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HyperfineTransitionFrequencyOfCs',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    