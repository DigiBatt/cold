
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class FrequencyResponseAnalyser(Device):
    """
    Class representing the `FrequencyResponseAnalyser` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_279ecc9f_bfbc_4108_ae40_3c1c0f735e60'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FrequencyResponseAnalyser'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FrequencyResponseAnalyser(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_279ecc9f_bfbc_4108_ae40_3c1c0f735e60',
    
    class_name='FrequencyResponseAnalyser',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_279ecc9f_bfbc_4108_ae40_3c1c0f735e60',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FrequencyResponseAnalyser',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    