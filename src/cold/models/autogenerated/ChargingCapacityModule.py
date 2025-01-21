
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CapacityModule import Capacity







class ChargingCapacity(Capacity):
    """
    Class representing the `ChargingCapacity` entity, which inherits from:
    - Capacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10763eb0_dbc9_4d34_bd1a_7b8996590d45'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingCapacity'`
        - **Alias**: `class_name`
    
    - `biologicLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `biologicLabel`
    
    - `arbinLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `arbinLabel`
    
    - `maccorLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `maccorLabel`
    
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
    obj = ChargingCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10763eb0_dbc9_4d34_bd1a_7b8996590d45',
    
    class_name='ChargingCapacity',
    
    biologicLabel="example_value",
    
    arbinLabel="example_value",
    
    maccorLabel="example_value",
    
    batteryArchiveLabel="example_value",
    
    elucidation="example_value",
    
    newareLabel="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10763eb0_dbc9_4d34_bd1a_7b8996590d45',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingCapacity',
        alias="class_name"
    )
    
    biologicLabel: Optional[str] = Field(
        None,
        alias="biologicLabel"
    )
    
    arbinLabel: Optional[str] = Field(
        None,
        alias="arbinLabel"
    )
    
    maccorLabel: Optional[str] = Field(
        None,
        alias="maccorLabel"
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
    

    
    

    

    