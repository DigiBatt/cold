
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeModule import Time



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class TestTime(Time, ElectrochemicalQuantity):
    """
    Class representing the `TestTime` entity, which inherits from:
    - Time, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27b3799c_250c_4332_8b71_7992c4a7bb05'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TestTime'`
        - **Alias**: `class_name`
    
    - `arbinLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `arbinLabel`
    
    - `maccorLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `maccorLabel`
    
    - `indigoLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `indigoLabel`
    
    - `novonixLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `novonixLabel`
    
    - `batteryArchiveLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `batteryArchiveLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `newareLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `newareLabel`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TestTime(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27b3799c_250c_4332_8b71_7992c4a7bb05',
    
    class_name='TestTime',
    
    arbinLabel="example_value",
    
    maccorLabel="example_value",
    
    indigoLabel="example_value",
    
    novonixLabel="example_value",
    
    batteryArchiveLabel="example_value",
    
    elucidation="example_value",
    
    newareLabel="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27b3799c_250c_4332_8b71_7992c4a7bb05',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TestTime',
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
    
    indigoLabel: Optional[str] = Field(
        None,
        alias="indigoLabel"
    )
    
    novonixLabel: Optional[str] = Field(
        None,
        alias="novonixLabel"
    )
    
    batteryArchiveLabel: Optional[str] = Field(
        None,
        alias="batteryArchiveLabel"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    newareLabel: Optional[str] = Field(
        None,
        alias="newareLabel"
    )
    

    
    

    

    