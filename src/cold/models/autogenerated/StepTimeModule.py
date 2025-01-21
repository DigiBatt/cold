
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeModule import Time



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class StepTime(Time, ElectrochemicalQuantity):
    """
    Class representing the `StepTime` entity, which inherits from:
    - Time, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_80ca00f8_c891_4493_87a2_7d39b9d1e098'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StepTime'`
        - **Alias**: `class_name`
    
    - `arbinLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `arbinLabel`
    
    - `maccorLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `maccorLabel`
    
    - `novonixLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `novonixLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StepTime(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_80ca00f8_c891_4493_87a2_7d39b9d1e098',
    
    class_name='StepTime',
    
    arbinLabel="example_value",
    
    maccorLabel="example_value",
    
    novonixLabel="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_80ca00f8_c891_4493_87a2_7d39b9d1e098',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StepTime',
        alias="class_name"
    )
    
    arbinLabel: Optional[str] = Field(
        None,
        alias="arbinLabel"
    )
    
    maccorLabel: Optional[str] = Field(
        None,
        alias="maccorLabel"
    )
    
    novonixLabel: Optional[str] = Field(
        None,
        alias="novonixLabel"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    