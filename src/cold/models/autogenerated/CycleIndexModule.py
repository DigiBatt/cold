
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class CycleIndex(PureNumberQuantity, ElectrochemicalQuantity):
    """
    Class representing the `CycleIndex` entity, which inherits from:
    - PureNumberQuantity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5766a819_c319_48ba_ab9a_ce3bd8fedee8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CycleIndex'`
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
    obj = CycleIndex(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5766a819_c319_48ba_ab9a_ce3bd8fedee8',
    
    class_name='CycleIndex',
    
    biologicLabel="example_value",
    
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
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5766a819_c319_48ba_ab9a_ce3bd8fedee8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CycleIndex',
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
    

    
    

    

    